from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .forms import UserForm
from .models import CustomUser


class RegisterUser(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user.html', {"form": form})

    def post(self, request):
        form = UserForm(request.POST)
        user = CustomUser(
            form['fullname'].value(),
            form['username'].value(),
            form['phone'].value(),
            form['password'].value(),
            form['confirm_password'].value(),
        )
        user.save()
        user_name = form['username'].value()
        phone = form['phone'].value()
        form.is_valid()
        db_user = CustomUser.objects.filter(username=user_name)
        db_phone = CustomUser.objects.filter(phone=phone)
        if db_phone and db_user:
            raise 'This user or phone number exists'
        else:
            return redirect('submit')


def submit(request):
    return render(request, "register.html")

