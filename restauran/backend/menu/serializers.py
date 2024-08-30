from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "name",
            "image",
            "price",
            "ingredients",
        ]

    def to_representation(self, instance):
        """
        Customize the output representation of the serializer.
        """
        representation = super().to_representation(instance)
        # You can customize the representation here if needed
        return representation

    def validate_price(self, value):
        """
        Custom validation for the price field.
        """
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
