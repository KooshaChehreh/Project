from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from .forms import UserForm, OtpForm
from .models import User
from .utils import generateOTP
from django.contrib import messages
from django.contrib.auth import login


class RegisterUser(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        if request.method == 'POST':
            user = UserForm()
            if user.is_valid():
                request.session['verification_code'] = generateOTP()
                request.session['user_info'] = {
                    'username': user.cleaned_data['username'],
                    'password': user.cleaned_data['password1'],
                    'is_staff': user.cleaned_data['is_staff'],
                }
                return redirect('verify')
            else:
                messages.error(request, 'information should be completely filled')
                UserForm()


class HomeView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class VerifyView(View):
    def get(self, request):
        form = OtpForm()
        print(form)
        return render(request, 'verify.html', {'form': form})

    def post(self, request):
        form = OtpForm(request.POST)
        if form.is_valid():
            code = request.session['verification_code']
            if code == form.cleaned_data['code']:
                user = User(request.session.get('user_info'))
                user.save()
                login(request=request, user=user)
                return redirect('HomeView')
            else:
                messages.error(request, 'Wrong code!')
                return redirect('VerifyView')
        else:
            messages.error(request, 'Code field should be filled!')
            return redirect('VerifyView')

