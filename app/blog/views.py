from django.views.generic import (
    CreateView,
    ListView,
)

from .forms import TextPostForm
from .models import TextPost


class TextPostList(ListView):
    model = TextPost
    context_object_name = 'posts'


class TextPostCreate(CreateView):
    model = TextPost
    form_class = TextPostForm
