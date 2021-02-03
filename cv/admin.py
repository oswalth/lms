from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from cv.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'image_tag', 'snippet_tag', 'first_email', 'second_email']

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="100"/>')

    def snippet_tag(self, obj):
        snippet = obj.snippet
        if len(snippet) > 20:
            snippet = obj.snippet + '...'
        return mark_safe(f'<code>{snippet}</code>')

    def first_email(self, obj):
        return True

    def second_email(self, obj):
        return False

