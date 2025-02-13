from django.contrib import admin
from .models import Product, Size, Category, ProductImage, Brand


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Количество пустых форм для добавления изображений


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'available', 'created', 'updated')
    list_filter = ('category', 'available', 'created', 'updated')
    search_fields = ('title', 'description', 'brand',)
    prepopulated_fields = {'slug': ('title',)}  # Автозаполнение поля slug
    inlines = [ProductImageInline]


class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')
    prepopulated_fields = {'slug': ('title',)}  # Автозаполнение поля slug


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}  # Автозаполнение поля slug


admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(Brand, BrandAdmin)
