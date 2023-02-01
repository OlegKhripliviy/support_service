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
        "<int:pk>/",
        TicketAPISet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]
