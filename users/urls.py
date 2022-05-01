from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('create/', views.AccountCreateView.as_view(), name='create'),
    path('create_done/', views.create_done, name='create_done'),
]
