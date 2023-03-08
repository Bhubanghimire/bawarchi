from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from administration.form import SubscribeForm


# Create your views here.
class SubscribeFormView(FormView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return redirect('home')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return self.success_url

