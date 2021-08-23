from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    producer = models.CharField(max_length=30)
    manufacture_date = models.DateTimeField()
    expiration_date = models.DateTimeField()

    def __str__(self):
        return self.name
