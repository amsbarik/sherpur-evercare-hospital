from django.urls import path 
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('faqs/', views.faqs, name='faqs'),



    # admin panel urls 
     path("hero-overview/", views.hero_overview, name="hero_overview"),

]

