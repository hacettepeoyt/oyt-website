from django.views import View
from django.shortcuts import redirect, render


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
