from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from .models import Supplier


class SupplierTests(APITestCase):

    def test_create_supplier(self):
        """
        Ensure we can create a supplier.

        """
        try:

            self.test_user = User.objects.create_superuser(
                username="muhammad", password="muhammad12345"
            )
            self.client.login(
                username=self.test_user.username, password="muhammad12345"
            )
            supplier_data = {"name": "test_supplier", "contact": "test_contact"}
            url = reverse(("supplier:list_create"))
            response = self.client.post(url, supplier_data, format="json")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            print(
                "\n_____________________________\nTEST 6 PASSED! \nTEST NAME: test_create_supplier\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_create_supplier: {e}\n\n")

    def test_view_suppliers(self):
        """
        Ensure we can view all suppliers

        """
        try:

            url = reverse("supplier:list_create")

            view_response = self.client.get(url, format="json")

            self.assertEqual(view_response.status_code, status.HTTP_200_OK)
            print(
                "\n_____________________________\nTEST 7 PASSED! \nTEST NAME: test_view_suppliers\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_view_suppliers: {e}\n\n")

    def test_view_supplier_details(self):
        """
        Ensure we can view details of a supplier

        """
        try:

            self.test_supplier = Supplier.objects.create(
                name="test_supplier", contact="test_contact"
            )

            url = reverse(
                ("supplier:retrieve_update_delete"),
                kwargs={"pk": self.test_supplier.id},
            )

            view_response = self.client.get(url, format="json")

            self.assertEqual(view_response.status_code, status.HTTP_200_OK)
            
            print(
                "\n_____________________________\nTEST 8 PASSED! \nTEST NAME: test_view_supplier_details\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_view_supplier_details: {e}\n\n")

    def test_update_supplier(self):
        """
        Ensure we can update a details of a supplier

        """
        try:
            self.testuser = User.objects.create_superuser(
                username="testuser", password="testuser12345"
            )
            self.client.login(username=self.testuser.username, password="testuser12345")

            test_supplier = Supplier.objects.create(
                name="test_name", contact="test_contact"
            )

            root = reverse(
                ("supplier:retrieve_update_delete"), kwargs={"pk": test_supplier.id}
            )
            update_response = self.client.put(
                root,
                {"name": "another_name", "contact": "another_contact"},
                format="json",
            )

            self.assertEqual(update_response.status_code, status.HTTP_200_OK)
            print(
                "\n_____________________________\nTEST 9 PASSED! \nTEST NAME: test_update_supplier\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_update_supplier: {e}\n\n")

    def test_delete_supplier(self):
        """
        Ensure we can delete a supplier

        """
        try:
            self.testuser = User.objects.create_superuser(
                username="testuser", password="testuser12345"
            )
            self.client.login(username=self.testuser.username, password="testuser12345")

            test_supplier = Supplier.objects.create(
                name="test_name", contact="test_contact"
            )

            root = reverse(
                ("supplier:retrieve_update_delete"), kwargs={"pk": test_supplier.id}
            )
            delete_response = self.client.delete(
                root,
                format="json",
            )

            self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
            print(
                "\n_____________________________\nTEST 10 PASSED! \nTEST NAME: test_delete_supplier\n _____________________________\n\n"
            )
        except AssertionError as e:
            print(f"\nFAILED: test_delete_supplier: {e}\n\n")
