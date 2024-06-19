from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal


class Inventory(models.Model):
    name = models.CharField(
        verbose_name="Product Name",
        max_length=200,
        null=False,
        blank=False,
        help_text="Enter name of item",
    )
    description = models.TextField(
        verbose_name="Product Description",
        blank=True,
        null=True,
        help_text="Enter a detailed description of the item",
    )
    price = models.DecimalField(
        verbose_name="Product Price",
        validators=[
            MinValueValidator(Decimal("0.00")),
            MaxValueValidator(Decimal("1000.00")),
        ],
        max_digits=10,
        decimal_places=2,
        error_messages={
            "invalid": "Please enter a valid price",
            "null": "This field cannot be null",
        },
        null=False,
        default=0.00,
    )

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Inventory"
        verbose_name_plural = "Inventories"

    def __str__(self):
        return self.name

    def suppliers(self):
        # inventory_item = Inventory.objects.all().get(id=self.id)
        # item_suppliers = inventory_item.items_supplied.all()
        return [supplier.name for supplier in self.items_supplied.all()]
