from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.register(History)
admin.site.register(HistoryItem)
admin.site.register(ShippingAddress)