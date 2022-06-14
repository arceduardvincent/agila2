import time

from decimal import Decimal, ROUND_DOWN

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils import translation
from django.utils.functional import cached_property

from model_utils.fields import StatusField
from model_utils import Choices
from generic.models import BaseModel


class Booking(BaseModel):
    PAYMENT = Choices('cash', 'credit')
    STATUS = Choices('draft', 'ordered', 'done')
    customer = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    verbose_name=_('User'))
    payment_method = models.CharField(_('Payment Method'), choices=PAYMENT,
                                      default=PAYMENT.cash, max_length=16)
    status = StatusField(verbose_name=_('Status'), default=STATUS.draft)


class Cart(BaseModel):
    STATUS = Choices('draft', 'submitted', 'closed')

    booking = models.OneToOneField(Booking, verbose_name=_('Booking'),
                                   on_delete=models.CASCADE,)
    invoice_sent = models.BooleanField(verbose_name=_('Invoice Sent'),
                                       default=False)
    payment_received = models.BooleanField(verbose_name=_('Payment Received'),
                                           default=False)
    payment_amount = models.DecimalField(_('Payment Amount'), max_digits=16,
                                         decimal_places=2, default=0.00)
    discount_percentage = models.DecimalField(_('Discount %'), max_digits=8,
                                              decimal_places=2, default=0.00)
    discount_amount = models.DecimalField(_('Discount Amount'), max_digits=16,
                                          decimal_places=2, default=0.00)
    status = StatusField(verbose_name=_('Status'), default=STATUS.draft)


# class BookingStats(BaseModel):
#     booking = models.OneToOneField('oms.Booking', verbose_name=_('Booking'))
#     tax_setting = models.DecimalField(_('Store Tax Rate (%)'),
#                                       max_digits=16, decimal_places=2,
#                                       default=0.00)
#     net_amount = models.DecimalField(_('Net Amount'), max_digits=16,
#                                      decimal_places=2, default=0.00)
#     tax_amount = models.DecimalField(_('Tax Amount'), max_digits=16,
#                                      decimal_places=2, default=0.00)
#     sales_quantity = models.IntegerField(_('Quantity'), default=0)
#     total_amount = models.DecimalField(_('Total Amount'), max_digits=16,
#                                        decimal_places=2, default=0.00)
#     discount_percentage = models.DecimalField(_('Discount %'), max_digits=8,
#                                               decimal_places=2, default=0.00)
#     discount_amount = models.DecimalField(_('Discount Amount'), max_digits=16,
#                                           decimal_places=2, default=0.00)
#     total_discount = models.DecimalField(_('Total Discount'), max_digits=16,
#                                          decimal_places=2, default=0.00)
#     payment_amount = models.DecimalField(_('Payment Amount'), max_digits=16,
#                                          decimal_places=2, default=0.00)
#     orders = JSONField(_('Orders'), default=dict)

class Item(BaseModel):
    course = models.ForeignKey('lab.course', verbose_name=_('Course'),
                               on_delete=models.CASCADE)
    price = models.DecimalField(_('Price'), max_digits=9,
                                decimal_places=2, default=0.00)


class OrderItem(BaseModel):
    STATUS = Choices('draft', 'done', 'ordered', 'cancelled')
    cart = models.ForeignKey(Cart, verbose_name=_('Cart'),
                             on_delete=models.CASCADE,)
    # course = models.ForeignKey('lab.Course', verbose_name=_('Course'),
    #                            on_delete=models.CASCADE)
    item = models.ForeignKey(Item, verbose_name=_('Item'),
                             on_delete=models.CASCADE, null=True)
    # item_options = models.ManyToManyField(
    #     'sms.ItemOption', verbose_name=_('Item Options'), blank=True)
    quantity = models.IntegerField(_('Quantity'))
    cancelled = models.BooleanField(_('Item Cancelled'), default=False)
    status = StatusField(_('Status'), default=STATUS.draft)
