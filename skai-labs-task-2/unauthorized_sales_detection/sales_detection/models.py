from django.db import models

class ProductListing(models.Model):
    product_id = models.CharField(max_length=100)
    authorized_seller_id = models.CharField(max_length=100)

class SalesTransaction(models.Model):
    product_id = models.CharField(max_length=100)
    seller_id = models.CharField(max_length=100)
