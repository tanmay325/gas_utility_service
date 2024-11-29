from django.urls import path
from . import views

app_name = 'customer_portal'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]

