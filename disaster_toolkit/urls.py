from django.urls import path
from . import views

urlpatterns = [
    path('disaster-toolkit/', views.disaster_toolkit, name='disaster_toolkit'),
]