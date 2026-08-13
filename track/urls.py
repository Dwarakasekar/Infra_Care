from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('track-project/', views.track_project_view, name='track_project'),
]
