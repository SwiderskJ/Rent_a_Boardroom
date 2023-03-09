from django.shortcuts import render, redirect
from user_app.forms import UserCreateForm, LoginForm
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


class UserCreateView(View):

    def get(self, request):
        form = UserCreateForm()
        return render(request, 'user_create.html', context={'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            user = User.objects.create_user(
                username=data.get('login'),
                password=data.get('password'),
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                email=data.get('email'),
                is_staff=data.get('host')
            )

        return redirect(reverse('login'))


class LoginView(View):  # This class-based view handles requests for the login page.
    def get(self, request): # The GET method returns the login form.
        form = LoginForm()

        return render(request, 'login.html', context={
                'form': form
            }
        )

    def post(self, request):  # The POST method authenticates the user and redirect to hero list page.
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            username = data.get('username')
            password = data.get('password')

            # authentication
            user = authenticate(
                username=username,
                password=password,
            )

            if user:
                # log in
                login(request, user)

                return redirect(reverse('hero_list'))
            else:
                return redirect(reverse('login'))


class LogoutView(View):  # This view logs the user out of the application and returns a logout page to the client.
    def get(self, request):
        logout(request)

        return render(
            request,
            'logout.html'
        )
