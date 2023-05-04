from django.shortcuts import render, get_object_or_404
from .models import Room,Booking, Client
from .forms import RoomForm,BookingForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from datetime import datetime, timedelta


# Create your views here.


def rooms(request):
    rooms = Room.objects.all()

    return render(request, "hosting/display_rooms.html", {"rooms": rooms})


def room(request, pk):
    room = get_object_or_404(Room, id=pk)

    return render(request, "hosting/room_detail.html", {"room": room})


@login_required(login_url=reverse_lazy("accounts:login"))
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("hosting:dashboard"))
    else:
        form = RoomForm()
    return render(request, "hosting/create_room.html", {"form": form})


@login_required(login_url=reverse_lazy("accounts:login"))
def edit_room(request, pk):
    room_to_edit = get_object_or_404(Room, pk=pk)

    if request.method == "POST":
        form = RoomForm(request.POST, request.FILES, instance=room_to_edit)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("hosting:dashboard"))
    else:
        form = RoomForm(instance=room_to_edit)
    return render(
        request, "hosting/edit_room.html", {"form": form, "name": room_to_edit.name}
    )


@login_required(login_url=reverse_lazy("accounts:login"))
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    room.delete()
    return HttpResponseRedirect(reverse("hosting:dashboard"))


@login_required(login_url=reverse_lazy("accounts:login"))
def userRooms(request):
    my_id = request.user.id
    owner = User.objects.get(id=my_id)
    my_rooms = Room.objects.filter(owner=owner)
    paginator = Paginator(my_rooms, 1)
    page = request.GET.get("page")
    items = paginator.get_page(page)
    return render(request, "hosting/dashboard.html", {"rooms": items})



@login_required(login_url=reverse_lazy("accounts:login"))
@transaction.atomic
def book_room(request):
    room_id =request.POST.get('room')
    room = get_object_or_404(Room, pk=room_id)
    client_id=request.POST.get('client')
    client = get_object_or_404(Client, pk=client_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST)
        
        if form.is_valid():
            booking = form.save(commit=False)
            begin_date_string = request.POST.get('begin')
            end_date_string = request.POST.get('end')
        
            begin_date = datetime.strptime(begin_date_string, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_string, '%Y-%m-%d')
        
            duration = (end_date - begin_date).days
        
            booking.duration = duration
            booking.client = client
            booking.room = room
            
            # Check for double booking
            existing_bookings = Booking.objects.filter(
                Q(begin__lt=end_date) & Q(end__gt=begin_date) & Q(room=room)
            )
            if existing_bookings:
                message = f"Room {room} is already booked from {begin_date} to {end_date}."
                return render(request, "hosting/book_room.html", {"form": form, "error_message": message})
            
            # Save the booking and mark the room as occupied
            booking.save()
            room.occupied = True
            room.save()
          
            return HttpResponseRedirect(reverse("hosting:bookings"))
    else:
        form = BookingForm()
    
    return render(request, "hosting/book_room.html", {"form": form})
def show_bookings(request):
    bookings = Booking.objects.all()
    return render(request,"hosting/bookings.html",{"bookings":bookings})