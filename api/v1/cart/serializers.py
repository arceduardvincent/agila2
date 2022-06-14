from rest_framework import serializers
from marketplace.models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem