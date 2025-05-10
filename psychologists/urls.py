from django.urls import path
from . import views

urlpatterns = [
    path('', views.psychologists_list, name='psychologists_list'),
    path('psychologists/', views.psychologists_list, name='psychologists_list'),
]
