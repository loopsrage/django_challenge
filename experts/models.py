from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Experts(AbstractUser):
    """Model to define an Expert as an Identity"""

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    short_url = models.URLField(blank=True)

    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        """Overwritting str to print out first_name and last_name for display"""
        return "{} {}".format(self.first_name, self.last_name)