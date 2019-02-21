from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='business-home'),
    path('about/', views.about, name='business-about'),
]
