from generic import api
from rest_framework import permissions
from rest_framework import filters
from rest_framework.views import APIView
from . import serializers
from marketplace.models import OrderItem
from lab.models import Course
from django.contrib.auth.models import User

from marketplace import models


class OrderItemView(APIView):
    pass