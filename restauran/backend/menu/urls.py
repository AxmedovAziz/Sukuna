from django.urls import path
from .views import *

urlpatterns = [
    path(
        "create_menu/",
        create_menu_view,
        name="create_menu",
    )
]
