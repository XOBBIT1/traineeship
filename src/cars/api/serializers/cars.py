from rest_framework import serializers
from src.cars.models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["name", "description", "cars_details", "provider"]

    def validate(self, attrs):
        name = attrs.get("name", "")

        if not name.isalnum():
            raise serializers.ValidationError("Data Error")
        return attrs
