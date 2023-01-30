from django.urls import path

from users.api import UserAPISet

urlpatterns = [
    path(
        "",
        UserAPISet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:id_>/",
        UserAPISet.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
    ),
]
