from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solve/', include('solve.urls')),  # Include URLs from the scramble app
]