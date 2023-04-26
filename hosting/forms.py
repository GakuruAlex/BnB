from django import forms
from .models import Room

    
    
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['image', 'name', 'description', 'location', 'price', 'occupied', 'is_cleaned', 'owner']
