from django.urls import path
from .views import *
app_name='movieapp'

urlpatterns=[
    path('',view_movie,name='view_movie'),
    path('movie/<int:movie_id>',details,name='details'),
    path('add_movie/',add_movie,name='add_movie'),
    path('update_movie/<int:id>/',update_movie,name='update_movie'),
    path('delete_movie/<int:id>/',del_movie,name="delete_movie")
]