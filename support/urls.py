from django.urls import path
from . import views

urlpatterns = [
    path('customer-support/', views.customer_support_view, name='customer_support'),
]
