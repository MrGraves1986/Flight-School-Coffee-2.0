from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('contact_us', views.contact_us),
    path('about_us', views.about_us),
]