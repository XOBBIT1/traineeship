from src.cars.api.serializers.cars import (
    CarsSerializer,
    SalonByeCarSerializer,
    ProfileByeCarsSerializer,
)
from src.cars.models import Cars
from django.shortcuts import render
from rest_framework import generics, viewsets, views, status
from rest_framework.response import Response


class CarsView(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


class SalonByeCarsView(views.APIView):
    queryset = Cars.objects.all()
    serializer_class = SalonByeCarSerializer

    def get_object(self, pk):
        return Cars.objects.get(pk=pk)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_200_OK)


class ProfileByeCarsView(views.APIView):
    queryset = Cars.objects.all()
    serializer_class = ProfileByeCarsSerializer

    def get_object(self, pk):
        return Cars.objects.get(pk=pk)

    def patch(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_200_OK)
