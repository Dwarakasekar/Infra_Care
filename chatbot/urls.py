from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chat_view, name='chatbot'),
    path('chatbot/api/', views.chat_api, name='chatbot_api'),
]