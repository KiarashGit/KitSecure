from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from keycloak import KeycloakOpenID
from django.conf import settings
import requests
import json

User = get_user_model()


class KeycloakOIDCBackend(OIDCAuthenticationBackend):
    def create_user(self, claims):
        username = claims.get('preferred_username')
        email = claims.get('email', '')

        user = User.objects.create_user(
            username=username,
            email=email,
        )
        return user

    def update_user(self, user, claims):
        user.email = claims.get('email', user.email)
        user.save()
        return user


class KeycloakAuthentication(JWTAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        token = auth_header.split(" ")[1]
        try:
            keycloak_openid = KeycloakOpenID(server_url="http://localhost:8080/",
                                             client_id="KharazmiID",
                                             realm_name="Kharazmi",
                                             client_secret_key="N7FiFW0gebOn2rNmnELj9eXm1Jdg3coX")

            public_key = keycloak_openid.public_key()
            if not public_key:
                raise AuthenticationFailed("Unable to retrieve public key from Keycloak")

            public_key = f"-----BEGIN PUBLIC KEY-----\n{public_key}\n-----END PUBLIC KEY-----"
            options = {"verify_signature": True, "verify_aud": False, "exp": True}
            token_info = keycloak_openid.decode_token(token, key=public_key, options=options)

            user, _ = User.objects.get_or_create(username=token_info.get('preferred_username'))
            return (user, token_info)

        except Exception as e:
            raise AuthenticationFailed(f"Invalid token: {str(e)}")
