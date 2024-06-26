import os

from django.db import models


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    file_name = f"{instance.id}{ext}"
    return f"logo_image/{file_name}"


class SiteSetting(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان سایت')
    address = models.CharField(max_length=400, verbose_name='آدرس')
    phone = models.CharField(max_length=20, verbose_name='تلفن')
    mobile = models.CharField(max_length=20, verbose_name='تلفن همراه')
    fax = models.CharField(max_length=20, verbose_name='فکس')
    email = models.EmailField(max_length=50, verbose_name='ایمیل')
    about_us = models.TextField(verbose_name='درباره ما', null=True, blank=True)
    copy_right = models.CharField(verbose_name='متن کپی رایت', null=True, blank=True, max_length=200)
    logo_image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name='لوگو')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'مدیریت سایت'

    def __str__(self):
        return self.title
