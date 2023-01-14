from django.contrib import admin


class TimeStampReadonlyAdmin(admin.ModelAdmin):
    _FIELDS = ["created_at", "updated_at"]

    readonly_fields = _FIELDS
    list_display = ["header", "created_at", "updated_at"]
    list_filter = _FIELDS
    search_fields = _FIELDS
