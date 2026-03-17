
from django.urls import path

from . import views

urlpatterns = [
    # path('blogs/', views.blogs, name='blogs' ),
    # path('blog-details/<int:pk>/', views.blog_details, name='blog_details' ),

    # Hospital
    path('admin/hospital-list/', views.hospital_list, name='hospital_list'),
    path('admin/hospital/form/', views.hospital_form, name='hospital_create'),
    path('admin/hospital/update/<int:pk>/', views.hospital_form, name='hospital_update'),

    # Specialization
    path('admin/specialization-list/', views.specialization_list, name='specialization_list'),
    path('admin/specialization/form/', views.specialization_form, name='specialization_create'),
    path('admin/specialization/update/<int:pk>/', views.specialization_form, name='specialization_update'),

    # Doctor
    path('admin/doctor-list/', views.doctor_list, name='doctor_list'),
    path('admin/doctor/form/', views.doctor_form, name='doctor_create'),
    path('admin/doctor/update/<int:pk>/', views.doctor_form, name='doctor_update'),

    # Doctor Schedule
    path('admin/doctor-schedule-list/', views.doctor_schedule_list, name='doctor_schedule_list'),
    path('admin/doctor-schedule/form/', views.doctor_schedule_form, name='doctor_schedule_create'),
    path('admin/doctor-schedule/update/<int:pk>/', views.doctor_schedule_form, name='doctor_schedule_update'),
]