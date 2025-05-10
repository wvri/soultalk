from django.db import models

class Psychologist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    telegram_link = models.URLField(blank=True, null=True)
    is_free = models.BooleanField(default=False)  # Поле для бесплатных психологов
    country = models.CharField(max_length=100, default="Казахстан")  # Указываем страну

    def __str__(self):
        return self.name
