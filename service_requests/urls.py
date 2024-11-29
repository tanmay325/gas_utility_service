from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_request, name='create_request'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
    path('list/', views.request_list, name='request_list'),
]