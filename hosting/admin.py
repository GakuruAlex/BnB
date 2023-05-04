from django.contrib import admin

# Register your models here.
from .models import Room,Client

admin.site.register(Room)
admin.site.register(Client)