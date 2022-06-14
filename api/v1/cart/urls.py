from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = 'cart'

urlpatterns = [
    path('order/',
         viewsets.OrderItemView.as_view(),
         name='order_cart'),
]

