from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

class IMDILoginView(LoginView):
    template_name ='login.html'

class IMDILogoutView(LogoutView):
    template_name = 'logout.html'