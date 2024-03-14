from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import EnrollForm
from .models import Member
from utils import send_message_to_admin_room


class EnrollView(View):
    def get(self, request):
        ctx = {
            'form': EnrollForm()
        }
        return render(request, 'user/enroll.html', ctx)
        pass

    def post(self, request):
        form = EnrollForm(request.POST)

        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            member = Member.objects.filter(student_id=student_id).first()

            if member:
                for field in form.fields:
                    setattr(member, field, form.cleaned_data[field])

                member.save()
                messages.success(request, f'Üyelik bilgilerin güncellendi {member.first_name}!')
            else:
                member = form.save()
                messages.success(request, f'Aramıza hoş geldin {member.first_name}! En kısa süre içerisinde gruba'
                                          f'ekleyeceğiz.')

            send_message_to_admin_room(f"Someone used the enroll form:\n"
                                       f"----\n"
                                       f"Name: {form.cleaned_data['first_name']}\n"
                                       f"Surname: {form.cleaned_data['last_name']}\n"
                                       f"E-mail: {form.cleaned_data['email']}\n"
                                       f"----\n"
                                       f"{form.cleaned_data['message']}")
            return redirect('home')
        else:
            ctx = {
                'form': EnrollForm(request.POST)
            }
            return render(request, 'user/enroll.html', ctx)
