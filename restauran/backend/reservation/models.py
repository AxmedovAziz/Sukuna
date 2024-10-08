from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time} ({self.id})"

    class Meta:
        permissions = [
            ("view_mymodel", "Can view my model"),
            ("edit_mymodel", "Can edit my model"),
            ("delete_mymodel", "Can delete my model"),
        ]
