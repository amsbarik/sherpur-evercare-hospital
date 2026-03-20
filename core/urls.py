from django.urls import path 
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('faqs/', views.faqs, name='faqs'),



    # admin panel urls 
     path("admin/hero-overview/form/", views.hero_overview_form, name="hero_overview_form"),
     path("admin/site-setting/form/", views.site_setting_form, name="site_setting_form"),

]

