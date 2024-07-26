from django.contrib import admin
from django.urls import path, include
from .views import landing_page, about, contact, menu_page  # Import specific views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("menu_page/", menu_page, name="menu_page"),
    path("reser/", include("reservation.urls")),
    path("menu-cr/", include("menu.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = "landing_page"
LOGIN_URL = "account_login"
LOGOUT_URL = "account_logout"
SIGNUP_REDIRECT_URL = "landing_page"
SIGNUP_URL = "account_signup"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_EMAIL_VERIFICATION = "none"
