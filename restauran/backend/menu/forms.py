from django import forms
from .models import Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            "name",
            "image",
            "price",
            "ingredients",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter menu name",
                    "id": "id_name",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter the price of food",
                }
            ),
            # "time": forms.TimeInput(
            #     attrs={"class": "form-control", "placeholder": "Time", "type": "time"}
            # ),
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter description",
                    "rows": 4,
                }
            ),
        }


def add_to_favorites(request, pk: int) -> bool:
    favorites = request.session.get("favorites", [])
    if pk not in favorites:
        favorites.append(pk)
        request.session["favorites"] = favorites
        return True
    return False  # Return False if pk is already in favorites


def remove_from_favorites(request, pk: int) -> bool:
    favorites = request.session.get("favorites", [])
    if pk in favorites:
        favorites.remove(pk)
        request.session["favorites"] = favorites
        return True
    return False
