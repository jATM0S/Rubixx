from django.urls import path, include
from .views import solve_cube_view,solve_kociemba_view,scramble_cube_view,execute_move_view

urlpatterns = [
    path('solve/', solve_cube_view , name='solve' ), 
    path('solve_kociemba/',solve_kociemba_view,name='kociemba_solve'),
    path('scramble/',scramble_cube_view,name='scramble'),
    path('execute_move/',execute_move_view,name='execute_move')
]