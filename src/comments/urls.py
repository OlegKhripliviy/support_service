from django.urls import path

from comments.api import CommentsListAPI


urlpatterns =[
    path(
        "tickets/<int:ticket_id>/comments",
        CommentsListAPI.as_view
    )
]