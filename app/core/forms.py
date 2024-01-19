from django.forms import ModelForm
from .models import Contact, Appointment

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'