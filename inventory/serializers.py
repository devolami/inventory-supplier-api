from rest_framework import serializers
from .models import Inventory


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
        }

    def get_suppliers(self, obj):
        return obj.suppliers()
