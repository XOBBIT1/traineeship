from src.profile.api.serializers.profile import RegisterSerializer
from src.profile.models import Profile
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response



class RegisterView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
