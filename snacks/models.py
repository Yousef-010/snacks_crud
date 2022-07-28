from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Snack(models.Model):
    """
    create a table in the database with these columns names
    """
    title = models.CharField(max_length=256)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        """
        To represent the Title in a better way
        """
        return self.title

    def get_absolute_url(self):
        """
        Redirects to snack_detail page
        """
        return reverse("snack_detail", args=[str(self.id)])
