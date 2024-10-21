from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<str:order_number>/',
         views.order_history, name='order_history'),
    path('admin_management/',
         views.admin_management, name='admin_management'),
    path('order_history_list/',
         views.order_history_list, name='order_history_list'),
    path('order_management/',
         views.order_management, name='order_management'),
    path('order_management/<str:order_number>/update/',
         views.update_order_status, name='update_order_status'),
    path('order/delete/<order_number>/',
         views.delete_order, name='delete_order'),
]
