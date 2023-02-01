from django.contrib import admin
from django.utils.text import Truncator

from shared.django.admin import TimeStampReadonlyAdmin
from comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(TimeStampReadonlyAdmin):
    list_display = ['ticket', 'user', 'truncated_field']

    def truncated_field(self, obj):
        return Truncator(obj.body).chars(20, truncate='...')

    truncated_field.short_description = 'Body'
