from django.http import JsonResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet

from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.serializers import TicketLightSerializer, TicketSerializer


class TicketAPISet(ViewSet):
    @staticmethod
    def list(request):
        queryset = Ticket.objects.all()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data)

    @staticmethod
    def retrieve(request, id_: int):
        instants = Ticket.objects.get(id=id_)
        serializer = TicketSerializer(instants)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    @staticmethod
    def delete(request, id_: int):
        Ticket.objects.get(id=id_).delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        context: dict = {"request": self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, id_: int):
        instance = Ticket.objects.get(id=id_)

        context: dict = {"request": self.request}
        serializer = TicketSerializer(
            instance, data=request.data, context=context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)
