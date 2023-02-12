from django.urls import path

from comments.api import CommentsCreateAPI, CommentsListAPI

urlpatterns = [
    path("tickets/<int:ticket_id>/comments", CommentsListAPI.as_view()),
    path(
        "tickets/<int:ticket_id>/comments/create", CommentsCreateAPI.as_view()
    ),
]
