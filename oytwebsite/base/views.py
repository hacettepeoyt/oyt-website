import random

from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View

from base.forms import ContactForm
from base.models import Book, Faq, Movie
from user.models import BoardMember
from utils import send_message_to_admin_room


class HomeView(View):
    def get(self, request):
        return redirect('about')

    def post(self, request):
        pass


class AboutView(View):
    def get(self, request):
        ctx = {
            'title': 'Hakkımızda',
            'board_members': BoardMember.objects.all().order_by('role'),
        }
        return render(request, 'base/about.html', ctx)

    def post(self, request):
        pass


class FaqView(View):
    def get(self, request):
        ctx = {
            'title': 'Sıkça Sorulan Sorular',
            'faqs': Faq.objects.filter(is_active=True).order_by('created_at')
        }
        return render(request, 'base/faq.html', ctx)

    def post(self, request):
        pass


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)

        return render(request, 'base/contact.html', {
            'title': 'İletişim Formu',
            'form': form,
            'num1': num1,
            'num2': num2
        })

    def post(self, request):
        form = ContactForm(request.POST)
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        captcha = int(request.POST.get('captcha', 0))

        if form.is_valid() and captcha == (num1 + num2):
            send_message_to_admin_room(f"Someone used the contact form:\n"
                                       f"----\n"
                                       f"Name: {form.cleaned_data['first_name']}\n"
                                       f"Surname: {form.cleaned_data['last_name']}\n"
                                       f"E-mail: {form.cleaned_data['email']}\n"
                                       f"----\n"
                                       f"{form.cleaned_data['message']}")
            messages.success(request, 'Bizimle iletişime geçtiğin için teşekkürler!')
            return redirect('contact')
        elif captcha != (num1 + num2):
            form.add_error('captcha', 'Bi toplama işlemini bile yapamadın beceriksiz insan(?)')

        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)

        return render(request, 'base/contact.html', {
            'title': 'İletişim Formu',
            'form': form,
            'num1': num1,
            'num2': num2
        })


class BookshelfView(View):
    def get(self, request):
        ctx = {
            'title': 'Kitaplık',
            'books': Book.objects.filter(is_active=True).order_by('title'),
            'movies': Movie.objects.filter(is_active=True).order_by('title')
        }
        return render(request, 'base/bookshelf.html', ctx)

    def post(self, request):
        pass
