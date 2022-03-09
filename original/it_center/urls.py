from django.urls import path
from it_center import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('services/', views.service, name='services'),
    path('login/', views.TemplateView.as_view(template_name='login.html'), name='login'),
]



