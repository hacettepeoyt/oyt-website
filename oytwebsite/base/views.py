from django.views import View
from django.shortcuts import redirect, render

from .models import Faq


class HomeView(View):
    def get(self, request):
        return redirect('about')

    def post(self, request):
        pass


class AboutView(View):
    def get(self, request):
        return render(request, 'base/about.html')

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
