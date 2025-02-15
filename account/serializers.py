from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'personnel_code' , 'password']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ['username', 'email', 'personnel_code', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return user
        raise serializers.ValidationError("Invalid credentials")


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, data):
        """Ensure refresh token is valid before proceeding."""
        try:
            RefreshToken(data['refresh'])  # Check if the token is valid
        except TokenError:
            raise serializers.ValidationError("Invalid or expired refresh token")
        return data

    def save(self, **kwargs):
        """Blacklist the refresh token to prevent reuse."""
        try:
            refresh = RefreshToken(self.validated_data['refresh'])
            refresh.blacklist()
        except TokenError:
            raise serializers.ValidationError("Token is invalid or already blacklisted")
