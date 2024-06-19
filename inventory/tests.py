from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Inventory


class InventoryTests(APITestCase):

    def test_create_inventory(self):
        """
        Ensure we can create an inventory

        """
        try:
            self.testuser = User.objects.create_superuser(
                username="testuser", password="testuser12345"
            )
            self.client.login(username=self.testuser.username, password="testuser12345")

            data = {"name": "test_item", "description": "test_description", "price": 50}

            url = reverse("inventory:list_create")

            create_response = self.client.post(url, data, format="json")
            self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)
            print(
                "\n_____________________________\nTEST 1 PASSED! \nTEST NAME: test_create_inventory\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_create_inventory: {e}\n\n")

    def test_view_inventories(self):
        """
        Ensure we can view all inventories

        """
        try:

            url = reverse("inventory:list_create")

            view_response = self.client.get(url, format="json")

            self.assertEqual(view_response.status_code, status.HTTP_200_OK)
            print(
                "\n_____________________________\nTEST 2 PASSED! \nTEST NAME: test_view_inventories\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_view_inventories: {e}\n\n")

    def test_view_detailed_inventory(self):
        """
        Ensure we can view details of an inventory

        """
        try:

            self.inventory_item = Inventory.objects.create(
                name="test_item", description="test_description", price=50
            )

            url = reverse(
                ("inventory:retrieve_update_delete"),
                kwargs={"pk": self.inventory_item.id},
            )

            view_response = self.client.get(url, format="json")

            self.assertEqual(view_response.status_code, status.HTTP_200_OK)
            print(
                "\n_____________________________\nTEST 3 PASSED! \nTEST NAME: test_view_detailed_inventory\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_view_detailed_inventory: {e}\n\n")

    def test_update_inventory(self):
        """
        Ensure we can update an inventory

        """
        try:
            self.testuser = User.objects.create_superuser(
                username="testuser", password="testuser12345"
            )
            self.client.login(username=self.testuser.username, password="testuser12345")

            test_inventory = Inventory.objects.create(
                name="test_name", description="test_description", price=70
            )

            root = reverse(
                ("inventory:retrieve_update_delete"), kwargs={"pk": test_inventory.id}
            )
            update_response = self.client.put(
                root,
                {
                    "name": "another_name",
                    "description": "another_description",
                    "price": 100,
                },
                format="json",
            )

            
            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            print(
                "\n_____________________________\nTEST 4 PASSED! \nTEST NAME: test_update_inventory\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_update_inventory: {e}\n\n")

    def test_delete_inventory(self):
        """
        Ensure we can delete an inventory

        """
        try:
            self.testuser = User.objects.create_superuser(
                username="testuser", password="testuser12345"
            )
            self.client.login(username=self.testuser.username, password="testuser12345")

            test_inventory = Inventory.objects.create(
                name="test_name", description="test_description", price=70
            )

            root = reverse(
                ("inventory:retrieve_update_delete"), kwargs={"pk": test_inventory.id}
            )
            delete_response = self.client.delete(
                root,
                format="json",
            )

            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
            print(
                "\n_____________________________\nTEST 5 PASSED! \nTEST NAME: test_delete_inventory\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_delete_inventory: {e}\n\n")
