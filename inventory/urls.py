from .views import InventoryRetrieveUpdateDestroyView, InventoryListCreateView
from django.urls import path

app_name = "inventory"
urlpatterns = [
    path("", InventoryListCreateView.as_view(), name="list_create"),
    path(
        "<int:pk>/",
        InventoryRetrieveUpdateDestroyView.as_view(),
        name="retrieve_update_delete",
    ),
]
