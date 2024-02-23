from django.shortcuts import render
from django.views import View

from .models import Project


class ProjectListView(View):
    def get(self, request):
        ctx = {
            'projects': Project.objects.all()
        }
        return render(request, 'arge/arge.html', ctx)
