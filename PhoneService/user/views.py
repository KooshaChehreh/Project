from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, OtpForm, LoginForm
from .models import User
from .utils import generateOTP
from django.contrib import messages
from django.contrib.auth import login


class RegisterView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'register.html', {"form": form})

    def post(self, request):
        user = UserForm(request.POST)
        if user.is_valid():
            username = user['username']
            try:
                res = User.objects.get(username=username)
            except User.DoesNotExist:
                res = None
            if res is not None:
                messages.error(request, 'The username is not available for you!')
                return redirect('register')
            else:
                request.session['verification_code'] = generateOTP()
                request.session['user_info'] = {
                    'username': user['username'].value(),
                    'password': user['password'].value(),
                    'phone': user['phone'].value(),
                }
                phone = user['phone'].value()
                form = OtpForm()
                return render(request, 'verify.html', {'phone': phone, 'form': form})
        else:
            print('Password does not match')
            messages.error(request, 'Password does not match')
            form = UserForm()
            return render(request, 'register.html', {"form": form})


class HomeView(View):
    def get(self, request):
        return render(request, 'landing.html')

    def post(self, request):
        return render(request, 'landing.html')


class VerifyView(View):
    def get(self, request):
        form = OtpForm()
        return render(request, 'verify.html', {'form': form})

    def post(self, request):
        form = OtpForm(request.POST)
        print(form.cleaned_data['otp_code'])
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


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            res = User.objects.get(username=username)
        except User.DoesNotExist:
            res = None
        if res is None:
            print('res is none')
            messages.error(request, 'You do not have an account! Register please.')
            print('wtf')
            return redirect('login')
        # elif res['suspend']:
        #     pass
        else:
            if password == res.password:
                login(request=request, user=res)
                return redirect('HomeView')
            else:
                messages.error(request, 'Password is incorrect!')
                return redirect('login')
