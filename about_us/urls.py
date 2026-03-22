from django.urls import path 
from .import views


urlpatterns = [
    path('about-us/', views.about_us, name='about_us'),


    # admin panel urls 
    path('admin/about-us/', views.about_create_or_update, name='about_create_or_update'),

    # path('admin/department-list/', views.department_list, name='department_list'),
    # path('admin/department/form/', views.department_form, name='department_create'),
    # path('admin/department/update/<int:pk>/', views.department_form, name='department_update'),

]

