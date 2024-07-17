# from  import add_to_favorites, remove_from_favorites
from django.shortcuts import render, redirect
from .forms import MenuForm
from .hello import add_to_favorites, remove_from_favorites


def create_menu_view(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("menu_page")
    else:
        form = MenuForm()

    context = {"form": form}
    return render(request, "create_menu.html", context)


def add_to_wishlist(request, pk):
    if request.method == "POST":
        if add_to_favorites(request, pk):
            return redirect("menu_page")  # Redirect to menu_page upon success
        else:
            # Handle failure scenario, if necessary
            return redirect("menu_page")
    else:
        print(request, "error")
        return redirect("menu_page")  # Redirect GET requests to menu_page


def remove_from_wishlist(request, pk):
    if request.method == "POST":
        if remove_from_favorites(request, pk):
            return redirect("menu_page")  # Redirect to menu_page upon success
        else:
            # Handle failure scenario, if necessary
            return redirect("menu_page")
    else:
        print(request, "error")
        return redirect("menu_page")  # Redirect GET requests to menu_page
