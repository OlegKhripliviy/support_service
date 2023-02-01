from django.urls import include, path

urlpatterns = [
    path("tickets/", include("tickets.urls")),
    path("comments/", include("comments.urls"))
]
