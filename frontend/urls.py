from django.urls import path, include
from frontend.views import HomeView, ContactView


urlpatterns = [
    path('', HomeView.as_view()),
    path('contact', ContactView.as_view(), name="contact_us")
]