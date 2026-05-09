from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Book

@admin.register(Book)
class SiteAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'user', 'added_on')
    search_fields = ['title']
    list_filter = ('added_on',)
    prepopulated_fields = {'title': ('title',)}
    summernote_fields = ('content',)
