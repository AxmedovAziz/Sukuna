from django.urls import path
from .views import *

urlpatterns = [
    path("", reservation_view, name="reservation"),
    path("blog", blog, name="blog"),
    path(
        "update-reservation/<int:pk>/",
        update_reservation_view,
        name="update_reservation_view",
    ),
    path(
        "reservations/delete/<int:pk>/",
        delete_reservation_view,
        name="delete_reservation",
    ),
]
