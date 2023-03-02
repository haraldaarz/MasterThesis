from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='scan-home'),
    path('startscan/', views.Startscan, name='scan-startscan'),
    path('startscan/external', views.external),
    path('startscan/custom', views.custom),
    path('defaultscan/', views.defaultscan, name='scan-defaultscan'),
    path('customports/', views.customports, name='scan-customports'),
    path('customcommand/', views.customcommand, name='scan-customcommand'),
    path('customports/custom', views.custom),
    path('defaultscan/external', views.external),
    
]
