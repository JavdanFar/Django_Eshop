from django.contrib import admin

# Register your models here.

from .models import Product, ProductGallery, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'active']

    class Meta:
        model = Product


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_comment', 'is_active']
    list_editable = ['is_active']

    class Meta:
        model = Comment


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)
admin.site.register(Comment, CommentAdmin)
