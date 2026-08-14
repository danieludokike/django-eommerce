from django.contrib import admin
from .models import Category, Product, Order, OrderItem, ShippingAddress

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created_at']
    list_filter = ['available', 'created_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class ShippingAddressInline(admin.StackedInline):
    model = ShippingAddress

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'paid', 'total_price', 'created_at']
    list_filter = ['paid', 'created_at']
    inlines = [OrderItemInline, ShippingAddressInline]