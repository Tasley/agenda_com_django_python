from django.shortcuts import render, redirect  # redirect
from core.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, " : User or password is not valid.")
            return redirect('/')

@login_required(login_url='/login')
def event_list(request):
    user = request.user
    event = Event.objects.filter(user=user)
    data = {'events': event}
    return render(request, 'agenda.html', data)
