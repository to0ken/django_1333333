from django.contrib import admin
from .models import Category, Product, Discount


@admin.register(Category)
class CatedoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category', 'price', 'available','created']
    list_filter =['available', 'created', 'category' ]
    list_editable = ['price','available']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_type', 'value', 'apply_to', 'product', 'active']
    list_editable = ['active']
    list_filter = ['active', 'discount_type']

    def get_type(self, obj):
        return '%' if obj.discount_type == 'percentage' else '₽'

    get_type.short_description = 'Тип'








