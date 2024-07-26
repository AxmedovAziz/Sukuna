from django.shortcuts import render, redirect
from menu.models import Menu


def landing_page(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def menu_page(request):
    menues = Menu.objects.all()
    price_less_than = Menu.price_less_than(50)
    with_meat = Menu.with_meat()

    context = {
        "menues": menues,
        "price_less_than": price_less_than,
        "with_meat": with_meat,
        "wishlist": request.session.get("favorites", []),
    }
    return render(request, "menu_page.html", context)
