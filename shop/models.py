from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    img = models.ImageField(upload_to='images/')
    price = models.PositiveBigIntegerField()
    rating = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    sales = models.PositiveBigIntegerField()