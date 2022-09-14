from rest_framework import serializers
from src.provider.models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["name", "description", "cars", "salons"]

    def validate(self, attrs):
        name = attrs.get("name", "")

        if not name.isalnum():
            raise serializers.ValidationError("Error")
        return attrs

