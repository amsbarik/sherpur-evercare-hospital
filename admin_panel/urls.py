from django.urls import path
from .views import AdminLoginView

from . import views

urlpatterns = [
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
]

