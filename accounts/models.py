from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.username

class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата и время")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.created_at.strftime('%Y-%m-%d %H:%M')}"
class PsychologyTip(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст совета")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at'] 

class Psychologist(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='psychologists/')
    description = models.TextField()
    whatsapp_number = models.CharField(max_length=20)

    def whatsapp_link(self):
        return f"https://wa.me/{self.whatsapp_number.replace('+', '').replace(' ', '')}"

    def __str__(self):
        return self.name