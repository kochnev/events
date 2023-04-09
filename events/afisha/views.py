from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Event


def index(request):
    age = request.GET.get('age')
    if age is None:
        events = Event.objects.filter(event_date__gte=timezone.now())
    else:
        for_kids = True if age == 'kids' else False
        events = Event.objects.filter(event_date__gte=timezone.now()).filter(for_kids=for_kids)

    events.order_by('event_date', 'time_from')
    return render(request, 'afisha/index.html', {'events': events, 'age': age})


def event_detail(request, event_id):
    e = get_object_or_404(Event, id=event_id)
    return render(request, 'afisha/event_detail.html', {'event': e})
