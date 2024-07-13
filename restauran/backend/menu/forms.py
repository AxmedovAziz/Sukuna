from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "image", "price", "ingredients", "time"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name of food"}
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the price of food",
                }
            ),
            "time": forms.TimeInput(
                attrs={"class": "form-control", "placeholder": "Time", "type": "time"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
