from django.urls import path
from .views import *

urlpatterns = [
    path("create-menu/", create_menu_view, name="create_menu"),
    path("add-to-wishlist/<int:pk>/", add_to_wishlist, name="add_to_wishlist"),
    path(
        "remove-from-wishlist/<int:pk>/",
        remove_from_wishlist,
        name="remove_from_wishlist",
    ),
    # Other paths
]
