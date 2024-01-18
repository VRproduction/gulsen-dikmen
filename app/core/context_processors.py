from .models import *
import datetime

def extras(request):
    context={
        'setting': GeneralSettings.objects.first(),
        'c_blogs': Blog.objects.all()[:2],
        'current_year': datetime.datetime.now().year
    }
    return context
