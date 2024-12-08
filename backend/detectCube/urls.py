from django.urls import path, include
from .views import scan_view

urlpatterns = [
    path('', scan_view,name='scan_cube'),  # Include URLs from the solve app

]