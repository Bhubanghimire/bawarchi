from django.urls import path, include
from frontend.views import HomeView, ContactView, ReserveView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', ContactView.as_view(), name="contact_us"),
    path('reserve', ReserveView.as_view(), name="reserve"),
]