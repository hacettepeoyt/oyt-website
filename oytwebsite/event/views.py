from django.shortcuts import render
from django.views import View

from event.models import Event, Course


class EventListView(View):
    def get(self, request):
        events = Event.objects.filter(is_active=True).order_by('-date')
        courses = Course.objects.filter(is_active=True).order_by('-date')

        # SQLite3 doesn't support ArrayField. Below, there is a simple trick to get over this problem.
        for course in courses:
            course.pre_requisites = course.pre_requisites.split(';') if course.pre_requisites else []

        ctx = {
            'title': 'Etkinlikler ve Kurslar',
            'events': events,
            'courses': courses,
        }
        return render(request, 'event/event_list.html', ctx)
