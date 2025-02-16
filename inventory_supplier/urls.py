from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Online Store Inventory and Supplier Management API",
        default_version="v1",
        description="The Inventory and Supplier Management API is designed to streamline and manage the inventory and supplier operations of an online store. This API supports various internal systems, including front-end interfaces and inventory tracking systems, ensuring efficient handling of inventory and supplier data.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="muhacodingresources@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=False,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("admin/", admin.site.urls),
    path("inventory/", include("inventory.urls")),
    path("supplier/", include("supplier.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
