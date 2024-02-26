from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Faq
from user.models import BoardMember


class HomeView(View):
    def get(self, request):
        return redirect('about')

    def post(self, request):
        pass


class AboutView(View):
    def get(self, request):
        ctx = {
            'board_members': BoardMember.objects.all().order_by('role')
        }
        return render(request, 'base/about.html', ctx)

    def post(self, request):
        pass


class FaqView(View):
    def get(self, request):
        ctx = {
            'faqs': Faq.objects.filter(is_active=True).order_by('created_at')
        }
        return render(request, 'base/faq.html', ctx)

    def post(self, request):
        pass


class ContactView(View):
    def get(self, request):
        ctx = {
            'form': ContactForm()
        }
        return render(request, 'base/contact.html', ctx)

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Thank you for contacting us!')
            # TODO: forward message to Matrix room
            return redirect('contact')
        else:
            ctx = {
                'form': ContactForm(request.POST)
            }
            messages.warning(request, 'Form is invalid!')
            return render(request, 'base/contact.html', ctx)
