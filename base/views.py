from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room, Topic, Message
from .forms import RoomForm, UserForm

def loginRegister(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "theres a problem with log in")


    context = {"page": page}
    return render(request, 'base/login_register.html', context)


def logoutuser(request):
    logout(request)
    return redirect("home")


def registeruser(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "theres a problem with log in")
    return render(request, "base/login_register.html", {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
            Q(name__icontains=q) |
            Q(description__icontains=q)
        )

    room_messages = Message.objects.all()
    room_count = rooms.count
    topics = Topic.objects.all()
    context = {"rooms": rooms, 'topics': topics, 'room_count': room_count, "room_messages": room_messages}
    return render(request, 'base/home.html', context)


def userprofile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {"user": user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, "base/user_profile.html", context) 


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        room_messages = Message.objects.create(
        user = request.user,
        room=room,
        body = request.POST.get("message.body")
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)
    context = {"room": room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/room.html', context)


@login_required(login_url="login")
def createroom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host = request.user,
            topic = topic,
            name = request.POST.get("name"),
            description = request.POST.get("description"),
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect("home")

    context ={"form": form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


@login_required(login_url="login")
def updateroom(request, pk):
    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()
    form = RoomForm(instance=room)

    if request.user != room.host:
       return HttpResponse('you are not allowed here')

    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get("name")
        room.topic = topic
        room.description = request.POST.get("description")
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid:
        #     form.save()
        return redirect('home')
    
    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)

@login_required(login_url="login")
def deleteroom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("you are not allowed here")

    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, 'base/delete.html', {'obj':room})
    

@login_required(login_url="login")
def deletemessage(request, pk):
    # room = Room.objects.all()
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("you are not allowed here")

    if request.method == "POST":
        message.delete()
        return redirect("home")
    return render(request, 'base/delete.html', {'obj':message})


@login_required(login_url='login')
def updateuser(request, pk):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userprofile', pk)

    context = {'user': user, 'form': form}
    return render(request, 'base/edituser.html', context)

