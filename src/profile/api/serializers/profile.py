from rest_framework import serializers
from src.profile.models import Profile


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, write_only=True)

    class Meta:
        model = Profile
        fields = ["email", "username", "password", "bio", "description"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")

        if not username.isalnum():
            raise serializers.ValidationError("Error")
        return attrs

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class EmailSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = Profile
        fields = ["token"]


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=555)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = Profile
        fields = ["email", "password"]
