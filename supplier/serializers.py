from rest_framework import serializers
from .models import Supplier


class SupplierSerializers(serializers.ModelSerializer):
    items = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Supplier
        fields = ["name", "contact", "items"]
        extra_kwargs = {
            "name": {"help_text": "Name of the supplier"},
            "contact": {"help_text": "Contact information of the supplier"},
            "items": {"help_text": "List of items supplied by the supplier"},
        }
