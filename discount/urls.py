from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_discount, name='create_discount'),
    path('', views.discount_list, name='discount_list'),
    path('edit/<int:discount_id>/', views.edit_discount, name='edit_discount'),
    path(
        'delete/<int:discount_id>/',
        views.delete_discount,
        name='delete_discount'
    ),
]
