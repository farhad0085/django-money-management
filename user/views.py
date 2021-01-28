from rest_framework.response import Response
from common.views import LoggerAPIView
from .serializers import LoginSerializer, UserSerializer, RegistrationSerializer
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

class LoginView(LoggerAPIView):
    """Class based view loggin in user and returning Auth Token."""

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        data = request.data
        serializer_obj = LoginSerializer(data=data)

        if serializer_obj.is_valid():
            username = serializer_obj.data['username']
            password = serializer_obj.data['password']

            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'}, status=401)

            token, _ = Token.objects.get_or_create(user=user)

            response_data = UserSerializer(user).data
            response_data["key"] = token.key

            return Response(response_data, status=200)

        return Response(serializer_obj.errors, status=400)


class LogoutView(LoggerAPIView):
    """Logout user and remove token"""

    def post(self, request):
        Token.objects.get_or_create(user=request.user)[0].delete()
        return Response({"message": "Logged out"}, 200)


class UserInfo(LoggerAPIView):
    """Check the userinfo of a user"""

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class RegistrationView(CreateAPIView):
    """Registration view for creating new user"""

    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        token, _ = Token.objects.get_or_create(user=user)

        response_data = UserSerializer(user).data
        response_data["key"] = token.key

        return Response(response_data, 201)

    def perform_create(self, serializer):
        user = serializer.save(request=self.request)
        return user