from django.contrib import admin
from .models import Psychologist

@admin.register(Psychologist)
class PsychologistAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_free', 'country', 'whatsapp_number', 'telegram_link')
    search_fields = ('name', 'country')
