from django.contrib import admin  # noqa  F401

from shared.django.admin import TimeStampReadonlyAdmin
from tickets.models import Ticket


@admin.register(Ticket)
class TicketsAdmin(TimeStampReadonlyAdmin):
    list_display = ["id", "header", "body"]
