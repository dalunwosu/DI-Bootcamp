from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm, ProfileForm
from django.views.generic import FormView, DetailView
from .models import Profile
class IMDILoginView(LoginView):
    template_name ='login.html'

class IMDILogoutView(LogoutView):
    template_name = 'logout.html'

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    def get_success_url(self) -> str:
        return reverse('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ProfileCreateView(FormView):
    template_name = 'profile_create.html'
    form_class = ProfileForm

    def get_initial(self): #allows putting data into the ProfileForm in advance
        initial = super().get_initial()
        initial['user'] = self.request.user.id
        return initial

    def get_success_url(self) -> str:
        return reverse('profile',args=[self.request.user.profile.id])
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = Profile

