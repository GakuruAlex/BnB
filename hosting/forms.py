from django import forms
from .models import Room,Booking,User
from django.shortcuts import get_object_or_404

    
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['image', 'name', 'description', 'location', 'price', 'occupied', 'is_cleaned', 'owner']




class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client','room','begin','end']
        
        widgets = {
            'begin': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'}),
        }
        
        
