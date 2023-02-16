from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.views.generic import ListView, CreateView


# Create your views here
class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = 'contact-us.html'


class ReserveView(TemplateView):
    template_name = 'reserve.html'


class AboutView(TemplateView):
    template_name = 'about.html'