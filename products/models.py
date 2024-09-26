from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
    
    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Increased max_digits to allow for larger prices
    image_url = models.URLField(max_length=255, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.name