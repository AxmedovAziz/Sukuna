from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone_number", "email", "guests", "date", "time"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "guests": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Guests"}
            ),
            "date": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Date", "type": "date"}
            ),
            "time": forms.TimeInput(
                attrs={"class": "form-control", "placeholder": "Time", "type": "time"}
            ),
        }


class UpdateReservation(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "phone_number", "email", "guests", "date", "time"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Name"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "guests": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Guests"}
            ),
            "date": forms.DateInput(
                attrs={"class": "form-control", "placeholder": "Date", "type": "date"}
            ),
            "time": forms.TimeInput(
                attrs={"class": "form-control", "placeholder": "Time", "type": "time"}
            ),
        }
