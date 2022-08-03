from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Event


def index(request):
    events = Event.objects.filter(event_date__gte=timezone.now()).order_by('event_date')
    #events = Event.objects.all().order_by('date_from')
    return render(request, 'afisha/index.html', {'events': events})


def event_detail(request, event_id):
    e = get_object_or_404(Event, id=event_id)
    return render(request, 'afisha/event_detail.html', {'event': e })
