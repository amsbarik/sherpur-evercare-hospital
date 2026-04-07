from django.urls import path 
from .import views


urlpatterns = [
    path('blood-donors/', views.blood_donors, name='blood_donors'),
    path('blood-donor-form/', views.blood_donor_form, name='blood_donor_form'),


    # admin panel urls 
    path('admin/blood-donor-list/', views.blood_donor_list, name='blood_donor_list'),
    path('admin/blood-donor/form/', views.blood_donor_create_or_update, name='blood_donor_create'),
    path('admin/blood-donor/update/<int:pk>/', views.blood_donor_create_or_update, name='blood_donor_update'),

]

