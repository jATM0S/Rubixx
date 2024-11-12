from django.urls import path, include
from .views import solve_cube_view

urlpatterns = [
    path('', solve_cube_view , name='solve' ),  # Include URLs from the scramble app
]