from django.urls import path 
from .import views


urlpatterns = [
    # path('services/', views.services, name='services'),


    # admin panel urls 
    path('admin/department-list/', views.department_list, name='department_list'),
    path('admin/department/form/', views.department_form, name='department_create'),
    path('admin/department/update/<int:pk>/', views.department_form, name='department_update'),

    path('admin/service-list/', views.service_list, name='service_list'),
    path('admin/service/form/', views.service_form, name='service_create'),
    path('admin/service/update/<int:pk>/', views.service_form, name='service_update'),

]

