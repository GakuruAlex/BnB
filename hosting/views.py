from django.shortcuts import render,get_object_or_404
from .models import Room
from .forms import RoomForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls  import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def rooms(request):
    rooms= Room.objects.all()
            
    return render(request,'hosting/display_rooms.html',{'rooms':rooms})





def room(request,pk):
    room = get_object_or_404(Room,id=pk)
    
    return render(request,"hosting/room_detail.html",{"room":room})
    

@login_required(login_url=reverse_lazy('accounts:login'))
def create_room(request):
    
    if request.method =='POST':
        form = RoomForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('hosting:dashboard'))
    else:
     form = RoomForm()
    return render(request,'hosting/create_room.html',{'form':form})
     
@login_required(login_url=reverse_lazy('accounts:login'))   
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
    
    
    
    
@login_required(login_url=reverse_lazy('accounts:login'))
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return HttpResponseRedirect(reverse('hosting:dashboard'))


@login_required(login_url=reverse_lazy("accounts:login"))
def ownerRooms(request):
    my_id = request.user.id
    owner = User.objects.get(id=my_id)
    my_rooms = Room.objects.filter(owner=owner)
    
    return HttpResponse(request,"dashboard.html",my_rooms)