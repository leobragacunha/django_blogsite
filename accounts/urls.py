from django.urls import path 
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    path("signup/", views.signUpView, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("<int:pk>/update/", views.UpdateProfileView.as_view(), name='profile-update'),
    path("<int:pk>/delete/", views.DeleteProfileView.as_view(), name='profile-delete'),
]
