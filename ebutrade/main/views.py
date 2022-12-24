from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import exchangeInfo as ex
from .utils import DataMixin
from .models import APIKeys


def index(request):
    return render(request, 'main/index.html', {'btc': [ex.a1, ex.a2, ex.a3, ex.a4, ex.a5, ex.a6, ex.a7],
                                               'eth': [ex.b1, ex.b2, ex.b3, ex.b4, ex.b5, ex.b6, ex.b7],
                                               'bnb': [ex.c1, ex.c2, ex.c3, ex.c4, ex.c5, ex.c6, ex.c7],
                                               'sol': [ex.d1, ex.d2, ex.d3, ex.d4, ex.d5, ex.d6, ex.d7],
                                               'xrp': [ex.e1, ex.e2, ex.e3, ex.e4, ex.e5, ex.e6, ex.e7],
                                               'ltc': [ex.f1, ex.f2, ex.f3, ex.f4, ex.f5, ex.f6, ex.f7]
                                               })


def strategy(request):
    return render(request, 'main/strategy.html')


def calc(request):
    return render(request, 'main/calc.html')

def profile(request):
    keys = APIKeys.objects.all()
    return render(request, 'main/profile.html', {'keys': keys})


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

