import datetime
import jwt
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics, viewsets, status, views
from src.profile.api.serializers.profile import (
    RegisterSerializer,
    EmailSerializer,
    LoginSerializer,
)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from src.profile.models import Profile
from rest_framework.exceptions import AuthenticationFailed
from .utils import Util
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class RegisterView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data

        user = Profile.objects.get(email=user_data["email"])

        token = RefreshToken.for_user(user).access_token

        current = get_current_site(request)
        relativeLink = reverse("_email")
        absurls = "https://" + current + relativeLink + "?token=" + str(token)
        email_body = (
            "Hi"
            + user.username
            + " User link below to verify your email \n"
            + "domain"
            + absurls
        )
        data = {
            "email_body": email_body,
            "email_user": user,
            "email_subject": "Verify your email",
        }

        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerfyEmail(views.APIView):
    serializer_class = EmailSerializer

    token_param_config = openapi.Parameter(
        "token",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self):
        token = request.GET.get("token")
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = Profile.objects.get(id=payload["user_id"])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response(
                {"email": "Successfully activated"}, status=status.HTTP_200_OK
            )

        except jwt.ExpiredSignatureError as identifier:
            return Response({"error": "Activation"}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response(
                {"error": "Invalid token!"}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(views.APIView):
    serializer_class = LoginSerializer
    login_param = openapi.Parameter(
        "email",
        in_=openapi.IN_QUERY,
        description="Description",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(manual_parameters=[login_param])
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = Profile.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response()
        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}

        return response


class ProfileView(views.APIView):
    def get(self, request):
        token = request.COOKIES.get(jwt)

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            payload = jwt.decode(token, "secret", algorithm=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated!")

        user = Profile.objects.get(id=payload["id"]).first()
        serializar = RegisterSerializer(user)

        return Response(serializar.data)


class LogoutView(views.APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}

        return response

