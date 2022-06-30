from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    price = models.FloatField()
    dimensions = models.TextField(null=True, blank=True)
    colors = models.TextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    stock = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
