from django.shortcuts import render,get_object_or_404
from .models import Room
from .forms import RoomForm
from django.http import HttpResponseRedirect
from django.urls  import reverse
# Create your views here.

def rooms(request):
    rooms= Room.objects.all()
        
    return render(request,'hosting/display_rooms.html',{'rooms':rooms})





def room(request,pk):
    room = get_object_or_404(Room,id=pk)
    
    return render(request,"hosting/room_detail.html",{"room":room})
    


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
     
     
def edit_room(request,pk):
    room_to_edit = get_object_or_404(Room,pk=pk)
    
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room_to_edit.image= form.cleaned_data['image_url']
            room_to_edit.name = form.cleaned_data['name']
            room_to_edit.description =  form.cleaned_data['description']
            room_to_edit.location = form.cleaned_data['location']
            room_to_edit.price = form.cleaned_data['price']
            room_to_edit.occupied= form.cleaned_data['is_occupied']
            room_to_edit.is_cleaned =form.cleaned_data['is_cleaned']
             
           
            room_to_edit.save()
            return HttpResponseRedirect(reverse('hosting:dashboard'))
    else:
        form =RoomForm(initial={
            'image':room_to_edit.image,
            'name':room_to_edit.name,
            'description': room_to_edit.description,
            'location':room_to_edit.location,
            'price': room_to_edit.price,
            'occupied':room_to_edit.occupied,
            'is_cleaned': room_to_edit.is_cleaned
        })  
    return render(request,"hosting/edit_room.html",{"form":form,"name":room_to_edit.name})
    
    
    
    

def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return HttpResponseRedirect(reverse('hosting:dashboard'))