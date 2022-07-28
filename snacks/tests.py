from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Snack


class SnackTests(TestCase):
    def setUp(self):
        """
        create a tester user
        """
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )
        # create a record in the table
        self.snack = Snack.objects.create(
            title="pickle",
            purchaser=self.user,
            description="Salty snack",
        )

    def test_string_representation(self):
        """
        Tests string representation
        """
        self.assertEqual(str(self.snack), "pickle")

    def test_snack_content(self):
        """
        Test the record's data , title, purchaser and description
        """
        self.assertEqual(f"{self.snack.title}", "pickle")
        self.assertEqual(f"{self.snack.purchaser}", "tester")
        self.assertEqual(f"{self.snack.description}", "Salty snack")

    def test_snack_list_view(self):
        """
        Test the status_code, if contain the title and the TemplateUsed for snack_list page
        """
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        """
        Test the status_code, if contain the title and the TemplateUsed for snack_detail page
        """
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        """
        Test create new snack and the Redirections
        """
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Chocolate",
                "purchaser": self.user.id,
                "description": "Details about Chocolate",
            },
            follow=True,
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "Details about Chocolate")

    def test_snack_update_view_redirect(self):
        """
        Test update  and the Redirections
        """
        response = self.client.post(
            reverse("snack_update", args="1"),
            {
                "title": "Updated name",
                "description": "3",
                "purchaser": self.user.id,
            },
        )

        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        """
        Test the status_code for snack_delete page
        """
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)
