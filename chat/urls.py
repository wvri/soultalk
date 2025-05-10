from django.urls import path
from . import views

urlpatterns = [
    # Здесь имя view и имя маршрута должны совпадать
    path('', views.room_list, name='room_list'),
    path('<str:room_name>/', views.room_detail, name='room_detail'),
]
