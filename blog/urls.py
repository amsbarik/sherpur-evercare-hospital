
from django.urls import path

from . import views

urlpatterns = [
    path('blogs/', views.blogs, name='blogs' ),
    path('blog-details/<int:pk>/', views.blog_details, name='blog_details' ),

    #blogs urls | admin panel
    path('blog-categories/', views.blog_category_list, name='blog_category_list'),
    path('blog/category/form/', views.blog_category_form, name='blog_category_create'),
    path('blog/category/update/<int:pk>/', views.blog_category_form, name='blog_category_update'),
    # path('blog/category/delete/<int:pk>/', views.blog_category_delete, name='blog_category_delete'),

    path('blog-list/', views.blog_list, name='blog_list'),
    path('blog/form/', views.blog_form, name='blog_create'),
    path('blog/update/<int:pk>/', views.blog_form, name='blog_update'),
    # path('blog/delete/<int:pk>/', views.blog_delete, name='blog_delete'),
]