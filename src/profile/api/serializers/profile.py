from src.profile.models import Profile
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = Profile
        fields = ["email", "username", "password", "bio", "description", "cars"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")

        if not username.isalnum():
            raise serializers.ValidationError("Error")
        return attrs

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)
