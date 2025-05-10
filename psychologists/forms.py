from django import forms
from .models import Psychologist

class PsychologistForm(forms.ModelForm):
    class Meta:
        model = Psychologist
        fields = ['name', 'description', 'whatsapp_number', 'telegram_link', 'is_free', 'country']
