from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .forms import UserForm
from .models import User


class RegisterUser(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        user = UserForm(request.POST)
        user.save()
        user_name = user['username'].value()
        phone = user['phone'].value()
        user.is_valid()
        db_user = User.objects.filter(username=user_name)
        db_phone = User.objects.filter(phone=phone)
        if db_phone and db_user:
            raise 'User exists!'
        else:
            return redirect('home')


def home(request):
    return render(request, "home.html")

