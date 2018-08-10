from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView, TemplateView)

from .forms import TextPostForm
from .models import TextPost


class Index(TemplateView):
    template_name = 'index.html'


class TextPostList(ListView):
    model = TextPost
    context_object_name = 'posts'


class TextPostDetail(DetailView):
    model = TextPost
    context_object_name = 'post'


class TextPostCreate(CreateView):
    model = TextPost
    form_class = TextPostForm
    success_url = reverse_lazy('text-post-list')
