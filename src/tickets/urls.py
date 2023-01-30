from django.urls import path

from tickets.api import TicketAPISet

urlpatterns = [
    path(
        "",
        TicketAPISet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "<int:id_>/",
        TicketAPISet.as_view(
            {"get": "retrieve", "put": "update", "delete": "delete"}
        ),
    ),
]
