from django import forms
from django.forms import TextInput

from .models import TextPost


class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = (
            'title',
            'content',
        )
        widgets = {
            'title': TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
