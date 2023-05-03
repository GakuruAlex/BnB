from django.urls import path
from . import views

app_name='hosting'

urlpatterns = [
    path('',views.rooms,name="homepage"),
    path('view-rooms/',views.rooms,name="view-rooms"),
    path("view-myrooms/",views.userRooms,name="dashboard"),
    path('createroom/',views.create_room,name="createroom"),
    path('rooms/<int:pk>/',views.room,name="viewroom"),
    path('editroom/<int:pk>/',views.edit_room,name="editroom"),
    path('delete/<int:pk>/',views.delete_room, name="delete_room")
]
