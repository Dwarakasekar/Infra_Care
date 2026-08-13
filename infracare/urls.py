"""
URL configuration for infracare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('Home/',views.homepage, name='homepage'),
    path('About/',views.aboutpage, name='aboutpage'),
    path('weather/',include('weather.urls')),
    path('Client/',views.clientpage, name='client'),
    path('Org/',views.orgpage, name='org'),
    path('cc/',views.cc_view, name='cc'),
    path('Cp/', views.cp_view,name='cp'),
    path('learnaboutsustain/',include('sustain.urls')),
    path('support/', include('support.urls')),
    path('track/', include('track.urls')),
    path('advisor/', include('advisor.urls')),
    path('', include('disaster_toolkit.urls')),
    path('', include('chatbot.urls')),
]
