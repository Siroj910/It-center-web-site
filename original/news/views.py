from django.shortcuts import render
from django.views.generic import TemplateView
from news.models import News


class NewsView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = News.objects.all()
        return context


