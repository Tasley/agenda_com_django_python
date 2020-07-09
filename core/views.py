from django.shortcuts import render #redirect
from core.models import Event

# Create your views here.



# def index(request):
#     return redirect('/agenda/')

def event_list(request):
    ##user = request.user
    event = Event.objects.all() #filter(user=user)
    data = {'events':event}
    return render(request, 'agenda.html', data)