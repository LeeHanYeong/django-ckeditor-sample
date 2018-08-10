from ckeditor.fields import RichTextField
from django.db import models


class TextPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
