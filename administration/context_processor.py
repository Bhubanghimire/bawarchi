from administration.models import OpeningHours, About


def global_context(request):
    context = {
        "about": About.objects.first(),
        "openning_hour": OpeningHours.objects.all()
    }
    return context
