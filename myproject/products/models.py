
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # Назва віскі
    description = models.TextField()         # Опис
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Ціна
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Фото

    def __str__(self):
        return self.name
