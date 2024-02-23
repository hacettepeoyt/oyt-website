from django.shortcuts import render
from django.views import View

from .models import Event, Course


class EventListView(View):
    def get(self, request):
        events = Event.objects.filter(is_active=True)
        courses = Course.objects.filter(is_active=True)

        # SQLite3 doesn't support ArrayField. Below, there is a simple trick to get over this problem.
        for course in courses:
            course.pre_requisites = course.pre_requisites.split(';') if course.pre_requisites else []

        ctx = {
            'events': events,
            'courses': courses,
        }
        return render(request, 'event/event_list.html', ctx)
