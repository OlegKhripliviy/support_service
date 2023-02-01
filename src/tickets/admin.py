from django.contrib import admin  # noqa  F401
from django.utils.text import Truncator

from shared.django.admin import TimeStampReadonlyAdmin
from tickets.models import Ticket


@admin.register(Ticket)
class TicketsAdmin(TimeStampReadonlyAdmin):
    list_display = ["id", "header", "truncated_body"]
    list_display_links = ["id", "header"]

    def truncated_body(self, obj):
        return Truncator(obj.body).chars(100, truncate='...')

    truncated_body.short_description = 'body'
