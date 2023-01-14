from django.contrib import admin  # noqa  F401
from tickets.models import Ticket
from shared.django.admin import TimeStampReadonlyAdmin


@admin.register(Ticket)
class TicketsAdmin(TimeStampReadonlyAdmin):
    pass
