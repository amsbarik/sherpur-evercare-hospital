
from django.urls import path

from . import views

urlpatterns = [
    path('appointment/form', views.appointment, name='appointment' ),
    # path('blog-details/<int:pk>/', views.blog_details, name='blog_details' ),

    #blogs urls | admin panel
    # path('blog-categories/', views.blog_category_list, name='blog_category_list'),
    # path('blog/category/form/', views.blog_category_form, name='blog_category_create'),
    # path('blog/category/update/<int:pk>/', views.blog_category_form, name='blog_category_update'),
]