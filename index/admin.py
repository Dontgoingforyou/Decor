from django.contrib import admin

from index.forms import ProductForm
from index.models import Product, Category, SpecialOffers


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ("id", "name", "price", "category")
    list_editable = ("category",)
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(SpecialOffers)
class SpecialOffersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "discounted_price")
    list_editable = ("price", "discounted_price")
