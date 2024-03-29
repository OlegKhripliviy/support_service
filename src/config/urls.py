from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("exchange-rates/", include("exchange_rates.urls")),
    path("admin/", admin.site.urls),
    path("", include("tickets.urls")),
    path("", include("comments.urls")),
    path("users/", include("users.urls")),
    path("auth/", include("authentication.urls")),
]
