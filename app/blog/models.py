from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse


class TextPost(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('text-post-detail', kwargs={'pk': self.pk})
