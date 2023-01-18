from django.http import JsonResponse
from django.urls import path
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView

from tickets.models import Ticket
from tickets.serializers import TicketSerializer, TicketLightSerializer, TicketCreateSerializer


class TicketsGet(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketLightSerializer


def get_ticket(request, id_: int) -> JsonResponse:
    ticket: Ticket = Ticket.objects.get(id=id_)
    serializer = TicketSerializer(ticket)
    return JsonResponse(serializer.data)


@api_view(["POST"])
def create_ticket(request):
    serializer = TicketCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    Ticket.objects.create(**serializer.validated_data)
    return JsonResponse(serializer.validated_data)


urlpatterns = [
    path("", TicketsGet.as_view()),
    path("create/", create_ticket),
    path("<int:id_>", get_ticket)
]
