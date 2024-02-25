from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import *
from .forms import *

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat:chat_rooms')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat:chat_rooms')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('chat:login')


@login_required
def chat_rooms(request, room_name=None):
    if room_name:
        chat_room = get_object_or_404(ChatRoom, name=room_name)
        messages = Message.objects.filter(room=chat_room)
        form = MessageForm()
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.room = chat_room
                message.sender = request.user
                message.save()
                return redirect('chat:chat_rooms', room_name=room_name)  # Redirect to the same chat room after sending the message
        return render(request, 'message.html', {'chat_room': chat_room, 'messages': messages, 'form': form})
    else:
        chat_rooms = ChatRoom.objects.all()
        form = ChatRoomForm()
        if request.method == 'POST':
            form = ChatRoomForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('chat:chat_rooms')  # Redirect to chat_rooms page after creating a room
        return render(request, 'chat_rooms.html', {'chat_rooms': chat_rooms, 'form': form})


@login_required
def chat_room_messages(request, room_name):
    chat_room = get_object_or_404(ChatRoom, name=room_name)
    messages = Message.objects.filter(room=chat_room)
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = chat_room
            message.sender = request.user
            message.save()
            return redirect('chat:chat_room_messages', room_name=room_name)  # Redirect to the same chat room after sending the message
    return render(request, 'message.html', {'chat_room': chat_room, 'messages': messages, 'form': form})