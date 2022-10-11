"""Defines URL patterns for cosmetic_site."""
from django.urls import path
from . import views
app_name = 'cosmetic_site'
urlpatterns = [
# Home page
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'), 
    path('payment/', views.payment, name='payment'),
    path('failed/', views.failed, name='failed')  
]