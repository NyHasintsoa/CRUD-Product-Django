from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, {}, "home"),
    path('auth/login/', views.auth_user, {}, "auth_login"),
    path('auth/register/', views.auth_register, {}, "auth_register"),
    path('auth/logout/', views.auth_logout, {}, "auth_logout"),
]