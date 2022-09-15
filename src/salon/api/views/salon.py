from src.salon.models import Salon
from src.salon.api.serializers.salon import SalonSerializer
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response


class SalonView(viewsets.ModelViewSet):
    queryset = Salon.objects.all()
    serializer_class = SalonSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
