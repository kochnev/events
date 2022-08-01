from django.shortcuts import render
from .models import Event


def index(request):
    events = Event.objects.all().order_by('date_from')
    return render(request, 'afisha/index.html', {'events': events})
