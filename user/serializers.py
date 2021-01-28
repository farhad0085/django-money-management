from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'is_staff', 'is_superuser']


class RegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    full_name = serializers.CharField(max_length=60, required=False)
    phone = serializers.CharField(max_length=15, required=False)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        self.custom_signup(user)
        user.set_password(validated_data['password1'])
        user.save()
        return user

    def custom_signup(self, user):
        user.user_profile.phone_number = self.validated_data.get('phone', '')
        user.save()


class PasswordResetSerializer(serializers.Serializer):
    """
    Custom Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm
    

    def get_email_options(self):
        """Override this method to change default e-mail options"""

        extra_email_context = {
            "DEVELOPMENT": settings.ENVIRONMENT == 'development',
            "user_name": self.user.user_profile.name or self.user.username
        }
        return {
            'subject_template_name': 'reset-password-subject.txt',
            'html_email_template_name': 'reset-password-email.html',
            'email_template_name': 'reset-password-email.txt',
            'extra_email_context': extra_email_context
        }

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)
        
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError(_('No account found for that email address'))
        
        self.user = User.objects.get(email=value)
        
        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)