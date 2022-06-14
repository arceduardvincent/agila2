from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'payment_method', 'status')
    raw_id_fields = ("customer",)
    list_filter = ('status', )
    search_fields = ('customer__first_name', 'customer__last_name',
                     'customer__email', 'customer__username', )


admin.site.register(models.Cart)
admin.site.register(models.OrderItem)
