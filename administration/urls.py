from django.urls import path, include
from administration.views import SubscribeFormView

urlpatterns = [
    path('subscribe', SubscribeFormView.as_view(), name="subscribe")
    ]
