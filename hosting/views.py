from django.shortcuts import render,get_object_or_404
from .models import Room
from .forms import RoomForm
from django.http import HttpResponseRedirect
from django.urls  import reverse
# Create your views here.

def rooms(request):
    rooms= Room.objects.all()
        
    return render(request,'hosting/display_rooms.html',{'rooms':rooms})


def create_room(request):
    
    if request.method =='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            image =form.cleaned_data['image_url']
            name =form.cleaned_data['name']
            description = form.cleaned_data['description']
            location = form.cleaned_data['location']
            price = form.cleaned_data['price']
            occupied = form.cleaned_data['is_occupied']
            is_cleaned = form.cleaned_data['is_cleaned']
            
            my_room = Room(image=image,
                           name=name,
                           description=description,
                           location=location,
                           price = price,
                           occupied=occupied,
                           is_cleaned = is_cleaned
                           )
            
            my_room.save()
            return HttpResponseRedirect(reverse('hosting:dashboard'))
    else:
     form = RoomForm()
     return render(request,'hosting/create_room.html',{'form':form})
     


def room(request,pk):
    room = Room.objects.get(id=pk)
    return render(request,{"room":room},"hosting/room_detail.html")
    
    
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return HttpResponseRedirect(reverse('hosting:dashboard'))