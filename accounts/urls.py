from django.urls import path
from . import views
from .views import feedback_view

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('remove-avatar/', views.remove_avatar, name='remove_avatar'),
    path('feedback/', feedback_view, name='feedback'),
]
