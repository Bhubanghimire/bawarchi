from administration.models import OpeningHours, About
from administration.form import SubscribeForm


def global_context(request):
    context = {
        "about": About.objects.first(),
        "openning_hour": OpeningHours.objects.all(),
        "form": SubscribeForm
    }
    return context
