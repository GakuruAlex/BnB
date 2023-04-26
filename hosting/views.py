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
        form = RoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hosting:dashboard'))
    else:
     form = RoomForm()
    return render(request,'hosting/create_room.html',{'form':form})
     
     
def edit_room(request,pk):
    room_to_edit = get_object_or_404(Room,pk=pk)
    
    
    if request.method == 'POST':
        form = RoomForm(request.POST,request.FILES,instance=room_to_edit)
        if form.is_valid():
            form.save()            
            return HttpResponseRedirect(reverse('hosting:dashboard'))
    else:
        form =RoomForm(instance=room_to_edit)  
    return render(request,"hosting/edit_room.html",{"form":form,"name":room_to_edit.name})
    
    
    
    

def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return HttpResponseRedirect(reverse('hosting:dashboard'))