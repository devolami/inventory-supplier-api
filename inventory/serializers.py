from rest_framework import serializers
from .models import Inventory
from drf_yasg.utils import swagger_serializer_method


class InventorySerializers(serializers.ModelSerializer):

    suppliers = serializers.SerializerMethodField(
        help_text="List of suppliers for the inventory item"
    )

    class Meta:
        model = Inventory
        fields = ["name", "description", "price", "date_created", "suppliers"]

        extra_kwargs = {
            "name": {"help_text": "Name of the inventory item"},
            "description": {"help_text": "Description of the inventory item"},
            "price": {"help_text": "Price of the inventory item"},
            "date_created": {"help_text": "Date when the inventory item was created"},
            "suppliers": {"help_text": "Suppliers who supply the inventory items"},
        }

    @swagger_serializer_method(serializer_or_field=serializers.ListField)
    def get_suppliers(self, obj):
        return list(obj.suppliers())
