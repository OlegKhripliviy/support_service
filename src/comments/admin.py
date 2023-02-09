from django.contrib import admin
from django.utils.text import Truncator

from comments.models import Comment
from shared.django.admin import TimeStampReadonlyAdmin


@admin.register(Comment)
class CommentsAdmin(TimeStampReadonlyAdmin):
    list_display = ["id", "ticket", "user", "truncated_field"]

    def truncated_field(self, obj):
        return Truncator(obj.body).chars(20, truncate="...")

    truncated_field.short_description = "Body"  # type: ignore
