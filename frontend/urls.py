from django.urls import path, include
from frontend.views import HomeView, ContactView, ReserveView, AboutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about',AboutView.as_view(), name="about_us"),
    path('contact', ContactView.as_view(), name="contact_us"),
    path('reserve', ReserveView.as_view(), name="reserve"),
]