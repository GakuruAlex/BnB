from django import forms

class RoomForm(forms.Form):
    image_url = forms.CharField(label="Image url",required=False,min_length=25)
    name=forms.CharField(label="Room name", max_length=10, required=False)
    description =forms.CharField(label="Room Description")
    price = forms.FloatField( required=False)
    location =forms.CharField(label="Location", max_length=25, required=False)
    is_occupied = forms.BooleanField(required=False)
    is_cleaned = forms.BooleanField(required=False)
    
    
    
    
    