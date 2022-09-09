from rest_framework import serializers
from src.cars_details.models import CarsDetails


class CarsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsDetails
        fields = ["name", "description", "car_brand", "cars"]

    def validate(self, attrs):
        name = attrs.get("name", "")

        if not name.isalnum():
            raise serializers.ValidationError("Error")
        return attrs
