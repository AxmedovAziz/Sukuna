from django.db import models
from django.db.models import Q
from datetime import datetime


# Create your models here.
def get_current_time():
    return datetime.now().time()


class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.id})"

    @staticmethod
    def with_meat():
        meat_keywords = ["chicken", "beef", "pork", "lamb", "meat"]
        query = Q()
        for keyword in meat_keywords:
            query |= Q(ingredients__icontains=keyword)
        return Menu.objects.filter(query)

    @staticmethod
    def without_meat():
        meat_keywords = ["chicken", "beef", "pork", "lamb", "meat"]
        query = Q()
        for keyword in meat_keywords:
            query |= Q(ingredients__icontains=keyword)
        return Menu.objects.exclude(query)

    @staticmethod
    def price_greater_than(amount):
        return Menu.objects.filter(price__gt=amount)

    @staticmethod
    def price_less_than(amount):
        return Menu.objects.filter(price__lt=amount)
