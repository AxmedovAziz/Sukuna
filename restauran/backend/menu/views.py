from django.shortcuts import render, redirect
from .forms import MenuForm


def create_menu_view(request):
    form = MenuForm()
    context = {"form": form}

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("menu_page")
    return render(request, "create_menu.html", context)
