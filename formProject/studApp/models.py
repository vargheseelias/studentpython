from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=15)
    address=models.CharField(max_length=15)
    phone=models.IntegerField()
    course=models.CharField(max_length=15)
    def __str__(self):
        return self.name

