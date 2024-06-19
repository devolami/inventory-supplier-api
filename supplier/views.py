from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Supplier
from .serializers import SupplierSerializers

from drf_yasg.utils import swagger_auto_schema



class SupplierListCreateView(generics.ListCreateAPIView):
    serializer_class = SupplierSerializers
    queryset = Supplier.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve a list of suppliers",
        responses={200: SupplierSerializers(many=True)},
        tags=["Supplier"],
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve a list of suppliers
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new supplier",
        request_body=SupplierSerializers,
        responses={201: SupplierSerializers},
        tags=["Supplier"],
    )
    def post(self, request, *args, **kwargs):
        """
        Create a new supplier
        """
        return super().post(request, *args, **kwargs)


class SupplierRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializers
    queryset = Supplier.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(
        operation_description="Retrieve a supplier by ID",
        responses={200: SupplierSerializers},
        tags=["Supplier"],
    )
    def get(self, request, *args, **kwargs):
        """
        Retrieve a supplier by ID
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a supplier by ID",
        request_body=SupplierSerializers,
        responses={200: SupplierSerializers},
        tags=["Supplier"],
    )
    def put(self, request, *args, **kwargs):
        """
        Update a supplier by ID
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a supplier by ID",
        responses={204: "No Content"},
        tags=["Supplier"],
    )
    def delete(self, request, *args, **kwargs):
        """
        Delete a supplier by ID
        """
        return super().delete(request, *args, **kwargs)
