from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import EnrollForm
from .models import Member


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
                messages.success(request, f'Updated {member.first_name}!')
            else:
                member = form.save()
                messages.success(request, f'Welcome {member.first_name}!')

            # TODO: send message to Matrix room
            return redirect('home')
        else:
            ctx = {
                'form': EnrollForm(request.POST)
            }
            messages.warning(request, 'Invalid form!')
            return render(request, 'user/enroll.html', ctx)
