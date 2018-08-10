from django.contrib import admin

from .forms import TextPostForm
from .models import TextPost


class TextPostAdmin(admin.ModelAdmin):
    form = TextPostForm


admin.site.register(TextPost, TextPostAdmin)
