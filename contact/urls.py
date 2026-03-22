from django.urls import path 
from .import views


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact_us'),


    # admin panel urls 

    path('admin/contact-list/', views.contact_list, name='contact_list'),
    # path('admin/service/form/', views.service_form, name='service_create'),
    # path('admin/service/update/<int:pk>/', views.service_form, name='service_update'),

]

