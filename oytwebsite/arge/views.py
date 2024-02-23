from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import IdeaForm

from .models import Project


class ProjectListView(View):
    def get(self, request):
        ctx = {
            'projects': Project.objects.all()
        }
        return render(request, 'arge/arge.html', ctx)


class IdeaView(View):
    def get(self, request):
        ctx = {
            'form': IdeaForm()
        }
        return render(request, 'arge/idea.html', ctx)

    def post(self, request):
        form = IdeaForm(request.POST)

        if form.is_valid():
            # TODO: send message to Matrix room
            messages.success(request, 'Your idea has been delivered!')
            return redirect('home')
        else:
            ctx = {
                'form': IdeaForm(request.POST)
            }
            return render(request, 'arge/idea.html', ctx)
