from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView
from django.shortcuts import render
from django.views.generic import ListView, CreateView

from administration.form import ContactUsForm, ReserveForm
from administration.models import About, ContactUs, Gallery, Item, Staff, Testimonials
from system.models import ConfigChoice
from administration.form import SubscribeForm


# Create your views here


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['special_food'] = Item.objects.filter(is_special=True).order_by('updated_at')[0:4]
        context['category_list'] = ConfigChoice.objects.filter()
        context['item_list'] = Item.objects.all()
        context['staffs'] = Staff.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        context['order_form'] = ReserveForm
        return context

    def post(self, request, *args, **kwargs):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(request.META['HTTP_REFERER'])



class ContactView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('contact_us')


class ReserveView(TemplateView):
    template_name = 'reserve.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReserveForm
        return context

    def post(self, request, *args, **kwargs):
        form = ReserveForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
        else:
            print(form.errors)
            return redirect(request.META['HTTP_REFERER'])


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['staffs'] = Staff.objects.all()
        context['testimonials'] = Testimonials.objects.all()
        return context


class MenuView(ListView):
    model = Item
    template_name = 'menu.html'
    context_object_name = 'menu_list'
    paginate_by = 8


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'image_list'
    paginate_by = 2
