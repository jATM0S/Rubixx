from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solve.urls')),  # Include URLs from the solve app
    path('scan/',include('detectCube.urls')) #include URLs from the detect cube app
]