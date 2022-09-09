from rest_framework import serializers
from src.salon.models import Salon
from django_countries.widgets import CountrySelectWidget
from django_countries.serializers import CountryFieldMixin


class SalonSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Salon
        fields = ["name", "location", "name_client", "name_provider", "car"]
        widgets = {"location": CountrySelectWidget()}

    def validate(self, attrs):
        name = attrs.get("name", "")

        if not name.isalnum():
            raise serializers.ValidationError("Error")
        return attrs


