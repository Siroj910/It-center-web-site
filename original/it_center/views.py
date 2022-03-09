from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Courses, Img, Mentors


class HomePageView(TemplateView):
    template_name = 'index.html'


def service(request):
    courses = Courses.objects.all()
    return render(request, 'services.html', {'courses': courses})


class AboutPageView(generic.ListView):
    template_name = 'about.html'
    model = Img
    context_object_name = 'img_list'
    queryset = Img.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context['mentor_list'] = Mentors.objects.all()
        return context




