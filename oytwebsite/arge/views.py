from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from utils import send_message_to_admin_room
from .forms import IdeaForm

from .models import Project


class ProjectListView(View):
    def get(self, request):
        ctx = {
            'projects': Project.objects.all()
        }
        return render(request, 'arge/project_list.html', ctx)


class IdeaView(View):
    def get(self, request):
        ctx = {
            'form': IdeaForm()
        }
        return render(request, 'arge/idea.html', ctx)

    def post(self, request):
        form = IdeaForm(request.POST)

        if form.is_valid():
            send_message_to_admin_room(f"Someone used the idea form:\n"
                                       f"----\n"
                                       f"Name: {form.cleaned_data['first_name']}\n"
                                       f"Surname: {form.cleaned_data['last_name']}\n"
                                       f"E-mail: {form.cleaned_data['email']}\n"
                                       f"----\n"
                                       f"{form.cleaned_data['project_title']}\n\n"
                                       f"{form.cleaned_data['message']}")
            messages.success(request, 'Bu fikri ilgili kişilere ilettik. Epostalarını kontrol etmeyi unutma!')
            return redirect('home')
        else:
            ctx = {
                'form': IdeaForm(request.POST)
            }
            return render(request, 'arge/idea.html', ctx)
