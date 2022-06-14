from django.views.generic import TemplateView, ListView, View
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from lab.models import Course
from django.shortcuts import render
from marketplace.models import OrderItem, Cart, Booking, Item
from lab.models import Course
from django.contrib.auth.models import User
from decimal import Decimal

from .dashboard import AnonymousDashboard


class HomeView(TemplateView):
    template_name = 'audience/anonymous/dashboard.html'


class CheckoutView(View):
    template_name = 'audience/checkout.html'

    def get(self, request, *args, **kwargs):
        get_orders = OrderItem.objects.all()
        get_total = Decimal(0.00)
        for i in get_orders:
            get_total += i.item.price

        context = {
            'result': get_orders,
            'total': Decimal(get_total)
        }
        return render(self.request, self.template_name, context)


class OrderView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        name = request.user.first_name
        get_course = Course.objects.get(id=id)
        get_user = User.objects.get(username=name)

        booking = Booking.objects.create(
            payment_method='cash', status='draft', customer=get_user
        )
        create_cart = Cart.objects.create(booking=booking)
        create_item = Item.objects.create(course=get_course, price=26)
        order = OrderItem.objects.create(quantity=1, cart=create_cart,
                                         item=create_item)

        return redirect('/checkout')


class RemoveOrderView(View):

    def get(self, request, *args, **kwargs):
        id = kwargs['id']
        order = OrderItem.objects.get(id=id)
        order.delete()

        return redirect('/checkout')

