from django.shortcuts import render, redirect
from menu.models import Menu


def landing_page(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def menu_page(request):
    menu = Menu.objects.all()
    context = {"menu": menu}
    return render(request, "menu_page.html", context)
