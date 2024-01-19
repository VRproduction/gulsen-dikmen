from .models import *
import datetime

def extras(request):
    context={
        'setting': GeneralSettings.objects.first(),
        "f_services": Service.objects.all()[:6],
        'c_blogs': Blog.objects.all()[:2],
        'current_year': datetime.datetime.now().year
    }
    return context
