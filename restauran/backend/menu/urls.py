from django.urls import path
from .views import *

urlpatterns = [
    path("create-menu/", create_menu_view, name="create_menu"),
    # path("hello/", MenuListCreateAPIView.as_view(), name="create_menu"),
    path("hello/", create_menu_view, name="create_menu"),
    path("detail-menu/<int:pk>/", detail_menu, name="detail_menu"),
    path("add-to-wishlist/<int:pk>/", add_to_wishlist, name="add_to_wishlist"),
    path(
        "remove-from-wishlist/<int:pk>/",
        remove_from_wishlist,
        name="remove_from_wishlist",
    ),
    # Other paths
]
