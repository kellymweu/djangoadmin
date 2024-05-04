from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group

#Custom title for admin
admin.site.site_header = 'Kelly M Admin Dashboard'

#order of diplay in the admin dashboard
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.unregister(Group)
