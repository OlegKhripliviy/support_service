from rest_framework import serializers

from tickets.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class TicketLightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['customer', 'manager', 'header']


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["header", "body"]
