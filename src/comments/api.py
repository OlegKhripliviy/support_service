from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    get_object_or_404,
)

from comments.models import Comment
from comments.serializers import CommentSerializer
from tickets.models import Ticket
from users.constants import Role


class CommentsCreateAPI(CreateAPIView):
    serializer_class = CommentSerializer
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def get_queryset(self):
        ticket_id: int = self.kwargs[self.lookup_field]
        return Comment.objects.filter(ticket_id=ticket_id)


class CommentsListAPI(ListAPIView):
    serializer_class = CommentSerializer
    lookup_field = "ticket_id"
    lookup_url_kwarg = "ticket_id"

    def _get_tickets(self):
        role: Role = self.request.user.role

        if role == Role.ADMIN:
            return Ticket.objects.all()
        elif role == Role.MANAGER:
            return Ticket.objects.filter(manager=self.request.user)

        return Ticket.objects.filter(customer=self.request.user)

    def get_queryset(self):
        tickets = self._get_tickets()
        ticket = get_object_or_404(
            tickets,
            self.kwargs[self.lookup_field],
        )
        comments = ticket.comments.order_by("-created_at")

        return comments
