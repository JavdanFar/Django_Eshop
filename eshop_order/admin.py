from django.contrib import admin
from eshop_order.models import Order, OrderDetail, UserAddress
# Register your models here.

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(UserAddress)
