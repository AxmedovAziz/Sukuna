# from  import add_to_favorites, remove_from_favorites
from django.shortcuts import render, redirect
from .forms import MenuForm
from .hello import add_to_favorites, remove_from_favorites
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Menu


from rest_framework.response import Response
from .serializers import MenuSerializer
from rest_framework import generics


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


class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get("name")
        ingredients = serializer.validated_data.get("ingredients")
        if ingredients is None:
            ingredients = name
        serializer.save(user=self.request.user, ingredients=ingredients)


def create_menu_view(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.owner = request.user
            menu.save()
            return redirect("menu")
    else:
        form = MenuForm()

    context = {"form": form}
    return render(request, "create_menu.html", context)


def detail_menu(request, pk=None, *args, **kwargs):
    if request.method == "GET" and pk is not None:
        menu = get_object_or_404(Menu, pk=pk)  # Get the user object
        data = {
            "id": menu.id,
            "name": menu.name,
            "ingredients": menu.ingredients,
            "price": menu.price,
            "image": menu.image.url,
            # Add other fields as necessary
        }
        context = {"data": data}
        return render(request, "detail_menu.html", context)

    else:
        return JsonResponse({"error": "Invalid request"}, status=400)


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
