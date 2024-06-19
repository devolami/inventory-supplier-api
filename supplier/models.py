from django.db import models
from inventory.models import Inventory


class Supplier(models.Model):
    name = models.CharField(
        verbose_name="Full Name", max_length=250, help_text="Enter your full name"
    )
    contact = models.TextField(verbose_name="Contact Information")
    items = models.ManyToManyField(Inventory, related_name="items_supplied", blank=True)

    class Meta:
        db_table = "Supplier"

    def __str__(self):
        return f"{self.id}. {self.name}"

