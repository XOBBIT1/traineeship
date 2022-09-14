from src.provider.models import Provider
from src.provider.api.serializers.provider import ProviderSerializer
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response


class ProviderView(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
