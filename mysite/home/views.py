from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# class based view
# ------------------
class SignupInterfaceView(CreateView):
    template_name = 'home/signup.html'
    form_class = UserCreationForm
    success_url = '/smart/notes'

    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect("note_list")

        return super().get(request)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'






#function based view
# ------------------   
# def home(request):
#     return render(request, "home/welcome.html")

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})