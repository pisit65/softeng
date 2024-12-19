from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView
    
urlpatterns = [
    # Home Page
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='logout.html'), name='login'),
    
]
