from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "user",
        "first_publish_year",
        "added_on",
    )
    search_fields = (
        "title",
        "author",
        "open_library_key",
        "isbn",
    )
    list_filter = (
        "first_publish_year",
        "added_on",
    )
