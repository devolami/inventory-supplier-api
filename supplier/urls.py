from django.urls import path
from .views import SupplierListCreateView, SupplierRetrieveUpdateDestroyView

app_name = "supplier"
urlpatterns = [
    path("", SupplierListCreateView.as_view(), name="list_create"),
    path(
        "<int:pk>/",
        SupplierRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_delete",
    ),
]
