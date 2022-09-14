from django.shortcuts import render
from rest_framework import generics, viewsets
from src.cars.api.serializers.cars import CarsSerializer
from rest_framework.response import Response
from src.cars.models import Cars


class CarsView(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)
