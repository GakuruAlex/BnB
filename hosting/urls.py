from django.urls import path
from . import views

app_name='hosting'

urlpatterns = [
    path('',views.rooms,name="dashboard"),
    path('view-rooms/',views.rooms,name="view-rooms"),
    path('createroom/',views.create_room,name="createroom"),
    path('rooms/<int:pk>/',views.room,name="room"),
    path('delete/<int:pk>/',views.delete_room, name="delete_room")
]
