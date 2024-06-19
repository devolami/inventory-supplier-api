from rest_framework import generics, permissions
from .serializers import InventorySerializers
from .models import Inventory
from drf_yasg.utils import swagger_auto_schema


class InventoryListCreateView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InventorySerializers

    @swagger_auto_schema(
        operation_description="Retrieve a list of inventory items",
        responses={200: InventorySerializers(many=True)},
        tags=["Inventory"],
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve a list of inventory items
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new inventory item",
        request_body=InventorySerializers,
        responses={201: InventorySerializers},
        tags=["Inventory"],
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new inventory item
        """
        return super().post(request, *args, **kwargs)


class InventoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = InventorySerializers

    @swagger_auto_schema(
        operation_description="Retrieve an inventory item by ID",
        responses={200: InventorySerializers},
        tags=["Inventory"],
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve an inventory item by ID
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update an inventory item by ID",
        request_body=InventorySerializers,
        responses={200: InventorySerializers},
        tags=["Inventory"],
    )
    def put(self, request, *args, **kwargs):
        """
        Update an inventory item by ID
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete an inventory item by ID",
        responses={204: "No Content"},
        tags=["Inventory"],
    )
    def delete(self, request, *args, **kwargs):
        """
        Delete an inventory item by ID
        """
        return super().delete(request, *args, **kwargs)
