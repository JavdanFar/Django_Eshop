from django.db.models import Q
from django.db import models
import os
from django.utils import timezone
from eshop_products_category.models import ProductCategory


# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{file_name}"


def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/galleries/{file_name}"


class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_products_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name, active=True)

    def get_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).distinct()


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name='قیمت')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='عکس')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی ها')
    visit_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    objects = ProductsManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ', '-')}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name='عکس')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'

    def __str__(self):
        return self.title


class Comment(models.Model):
    product_comment = models.ForeignKey(Product, related_name='product_comment', on_delete=models.CASCADE, verbose_name='محصول')
    name = models.CharField(max_length=50, verbose_name='نام')
    comment = models.TextField(null=True, blank=True, verbose_name='متن')
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.name
