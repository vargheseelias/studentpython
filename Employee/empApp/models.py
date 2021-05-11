from django.db import models
from django.urls import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phn_number = models.IntegerField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("empApp:details", kwargs={'pk':self.pk})
