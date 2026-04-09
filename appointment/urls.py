
from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path('appointment/form', views.appointment, name='appointment' ),
    # path('blog-details/<int:pk>/', views.blog_details, name='blog_details' ),

    # path('appointment/book/', views.appointment_create_view, name='appointment'),

    path("appointment/book/", views.book_appointment, name="book_appointment"),

    path("ajax/load-doctors/", api_views.ajax_load_doctors, name="ajax_load_doctors"),
    path("ajax/load-schedules/", api_views.ajax_load_schedules, name="ajax_load_schedules"),

    # path('api/doctors-by-department/', api_views.doctors_by_department_api, name='doctors_by_department_api'),
    # path('api/schedules-by-doctor/', api_views.schedules_by_doctor_api, name='schedules_by_doctor_api'),

    #blogs urls | admin panel
    # path('blog-categories/', views.blog_category_list, name='blog_category_list'),
    # path('blog/category/form/', views.blog_category_form, name='blog_category_create'),
    # path('blog/category/update/<int:pk>/', views.blog_category_form, name='blog_category_update'),
]