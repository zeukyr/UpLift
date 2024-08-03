from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('Signout', views.Signout, name="Signout"),
    path('Forums', views.Forums, name="Forums"),
    path('about', views.about, name="about"),
    path('feedback', views.feedback, name="feedback"),
    path('riceu', views.riceu, name="riceu"),
    path('kingscollege', views.kingscollege, name="kingscollege"),
    path('uofsydney', views.uofsydney, name="uofsydney"),
]