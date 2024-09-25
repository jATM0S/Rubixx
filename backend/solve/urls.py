from django.urls import path
from . import views  # Correct import of views

urlpatterns = [
    path('', views.cube, name='some_view'),  
]