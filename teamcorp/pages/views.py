from django.shortcuts import render
from django.contrib.auth import authenticate, login as user_login, logout
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from . import views

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')
# def user_login(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         return render(request, 'calendar/dashboard.html')
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, 'calendar/login.html')
def calendar(request):
    return render(request, 'pages/calendar.html')
def homepage(request):
    return render(request, 'calendar/homepage.html')
def register(request):
    return render(request, 'pages/registration.html')
# def dashboard(request):
#     return render(request, 'calendar/homepage.html')
# def login(request):
#     return render(request, 'calendar/login.html')

