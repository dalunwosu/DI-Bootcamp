from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import RegistrationForm
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get_success_url(self) -> str:
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(LoginView):
    template_name ='login.html'




def dashboard(request):
    return render(request, 'dashboard.html')

def logout(request):
    return redirect('home')