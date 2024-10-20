from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<str:order_number>/', views.order_history, name='order_history'),
    path('admin_management', views.admin_management, name='admin_management'),
    path('order_history_list/', views.order_history_list, name='order_history_list'),
]