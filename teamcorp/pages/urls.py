from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login', views.user_login, name='user_login'),
    path('calendar', views.calendar, name='calendar'),
    path('homepage', views.homepage, name='homepage'),
    path('register', views.register, name='register'),
    # path('dashboard', views.dashboard, name='dashboard')
]