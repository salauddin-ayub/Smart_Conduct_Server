# project_name/urls.py

from django.contrib import admin
from django.urls import path, include
from authentication import swagger

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # Include the authentication app URLs
    # Your other app URLs
    path('swagger/', include(swagger)),  # Include the swagger URLs from the authentication app
]
