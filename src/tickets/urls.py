from django.urls import path
from tickets.serializers import TicketSerializer
from rest_framework.generics import ListAPIView
from tickets.models import Ticket


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


urlpatterns = [
    path("", TicketsGet.as_view())
]
