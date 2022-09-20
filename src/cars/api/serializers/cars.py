from rest_framework import serializers
from src.cars.models import Cars


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["name", "description",  "provider"]

    def validate(self, attrs):
        name = attrs.get("name", "")

        if not name.isalnum():
            raise serializers.ValidationError("Data Error")
        return attrs


class SalonByeCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["id", "salon"]


class ProfileByeCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["id", "profile"]