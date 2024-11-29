from django.contrib import admin
from django.urls import path, include
from customer_portal.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer_portal.urls')),
    path('service-requests/', include('service_requests.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
   
    
]
