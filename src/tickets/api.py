from tickets.serializers import (
    TicketSerializer,
    TicketLightSerializer,
)
from django.http import JsonResponse
from tickets.models import Ticket
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from shared.serializers import ResponseSerializer, ResponseMultiSerializer
from tickets.permissions import RoleIsAdmin, RoleIsUser, IsOwner, RoleIsManager


class TicketAPISet(ModelViewSet):
    queryset = Ticket.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [RoleIsUser]
        elif self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager]
        elif self.action == "retrieve":
            permission_classes = (IsOwner | RoleIsAdmin | RoleIsManager,)
        elif self.action == "update":
            permission_classes = [RoleIsManager | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsManager | RoleIsAdmin]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        context: dict = {"request": self.request}
        serializer = TicketSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TicketLightSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TicketSerializer(instance)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def update(self, request, *args, **kwargs):
        instance: Ticket = self.get_object()

        context: dict = {"request": self.request}
        serializer = TicketSerializer(instance, data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, *args, **kwargs):
        instance: Ticket = self.get_object()
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
