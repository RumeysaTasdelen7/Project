from django.contrib import admin
from order.models import Address, Product, Order

# Register your models here.

admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Order)