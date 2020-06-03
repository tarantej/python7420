from django.shortcuts import render
from . import views
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

# Create your views here.
@xframe_options_sameorigin
def cal(request):
    return render(request, 'calendar/index.html')
def dashboard(request):
    return render(request, 'calendar/homepage.html')
# def login(request):
#     return render(request, 'calendar/login.html')
