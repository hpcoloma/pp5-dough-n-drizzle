from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),

]
