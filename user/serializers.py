from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer(read_only=True)
    connect_status = serializers.SerializerMethodField('get_connect_status')

    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'is_staff', 'is_superuser']

    def get_connect_status(self, obj):
        """Get data source connect status for user, if user at least connected with one data source"""

        creds_analytics = obj.creds_google_analytics
        creds_adwords = obj.creds_google_adwords
        creds_shopify = obj.creds_shopify
        creds_facebook = obj.creds_facebook

        active_property = obj.analytics_properties.get_active_property(obj) if creds_analytics.token else None
        active_ad_account_adwords = obj.adwords_ad_accounts.get_active_account(obj) if creds_adwords.token else None
        active_store = obj.stores.get_active_store(obj) if creds_shopify.access_token else None
        active_ad_account_facebook = obj.facebook_ad_accounts.get_active_account(obj) if creds_facebook.access_token else None

        return bool(active_property or active_ad_account_adwords or active_store or active_ad_account_facebook)


class RegistrationSerializer(RegisterSerializer):

    name = serializers.CharField(
        error_messages={
            'required': 'Name is required',
            'blank': 'Please enter your name'
        }
    )
    phone = serializers.CharField(
        error_messages={
            'required': 'Phone number is required',
            'blank': "Please enter a valid phone number"
        }
    )
    email = serializers.EmailField(
        error_messages={
            'required': 'Email is required',
            'blank': "Please enter a valid email address"
        }
    )

    def custom_signup(self, request, user):
        user.user_profile.name = self.validated_data.get('name', '')
        user.user_profile.phone_number = self.validated_data.get('phone', '')
        # user.save(update_fields=['name'])
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