import time
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm, OtpForm, LoginForm
from .models import User
from .utils import generateOTP
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


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
                request.session['ver_time'] = time.time()
                request.session['user_info'] = {
                    'username': user['username'].value(),
                    'password': user['password1'].value(),
                    'phone': user['phone'].value(),
                }
                print(request.session['verification_code'])
                return redirect('verify')
        else:
            print(user.fields.keys())
            err = []
            for field in user.fields.items():
                print(field)
                for i in range(len(user.errors)):
                    try:
                        err.append(user.errors[f'{field[0]}'].as_data()[i])
                    except Exception:
                        pass
            print(err)
            form = UserForm()
            return render(request, 'register.html', {"form": form, 'error': err})


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
        if form.is_valid():
            if time.time() - request.session['ver_time'] < 120:
                code = request.session['verification_code']
                if code == form['otp_code'].value():
                    print(request.session['user_info']['username'])
                    user = User(username=request.session['user_info']['username'],
                                phone=request.session['user_info']['phone'])
                    user.set_password(request.session['user_info']['password'])
                    user.save()
                    messages.success(request, 'you have registered successfully')
                    login(request=request, user=user)
                    return redirect('home')
                else:
                    messages.add_message(request, messages.ERROR, 'Wrong code!')
                    form = OtpForm()
                    return render(request, 'verify.html', {'form': form})
            else:
                messages.warning(request, 'Code was expired!')
                form = OtpForm()
                return render(request, 'verify.html', {'form': form})
        else:
            messages.error(request, 'Code field should be filled!')
            return redirect('verify')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        """
        I did not use authenticate! tried to handle it by myself, I know how it works.
        """

        # user = authenticate(request, username=username, password=password)
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
                return redirect('home')
            else:
                messages.error(request, 'Password is incorrect!')
                return redirect('login')


class LogOutView(View):
    def get(self, request):
        return render(request, 'logout.html')

    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('login')
        else:
            messages.error(request, 'You are not logged in!')
            redirect('login')

