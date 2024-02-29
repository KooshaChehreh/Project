from django.contrib import admin
from django.urls import path
from .views import RegisterView, LoginView, VerifyView, LogOutView


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
