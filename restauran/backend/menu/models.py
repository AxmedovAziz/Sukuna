from django.db import models
from django.db.models import Q

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="menu_images/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField()
    time = models.TimeField()  # Add this line for the time field

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

    def like(self):
        self.likes += 1
        self.save()

    def dislike(self):
        self.dislikes += 1
        self.save()

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
