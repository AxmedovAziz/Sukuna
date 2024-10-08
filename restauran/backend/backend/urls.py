from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("contact/", contact, name="contact"),
    path("reser/", include("reservation.urls")),
    path("menu/", include("menu.urls"), name="menu"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("create_profile/", include("user.urls")),
    # path("accounts/google/login/", GoogleLoginView.as_view(), name="google_login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

LOGIN_REDIRECT_URL = "landing_page"
LOGIN_URL = "account_login"
LOGOUT_URL = "account_logout"
SIGNUP_REDIRECT_URL = "landing_page"
SIGNUP_URL = "account_signup"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_EMAIL_VERIFICATION = "none"
# "ENGINE": "django.db.backends.postgresql",
#         "NAME": "railway",
#         "USER": "postgres",
#         "PASSWORD": "XFlaeDLoQeEzYwoPJgRfzEBKAWwSYnaY",
#         "HOST": "postgres.railway.internal",
#         "PORT": "5432",
