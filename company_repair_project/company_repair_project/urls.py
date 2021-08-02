from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients_app.urls')),
    path('clients/', include('django.contrib.auth.urls')),
    path('requests/', include('requests_app.urls')),
]
