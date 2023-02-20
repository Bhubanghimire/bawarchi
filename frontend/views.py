from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from administration.form import ContactUsForm
from administration.models import About, ContactUs, Gallery, Item


# Create your views here
class HomeView(TemplateView):
    template_name = "index.html"


class ContactView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('contact_us')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context



class ReserveView(TemplateView):
    template_name = 'reserve.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class MenuView(ListView):
    model = Item
    template_name = 'menu.html'
    context_object_name = 'menu_list'


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'image_list'
    paginate_by = 2