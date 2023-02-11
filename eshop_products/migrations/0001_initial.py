# Generated by Django 3.2 on 2023-02-11 10:09

from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='عکس')),
                ('active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('visit_count', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('categories', models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=eshop_products.models.upload_gallery_image_path, verbose_name='عکس')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'عکس',
                'verbose_name_plural': 'عکس ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='متن')),
                ('is_active', models.BooleanField(default=False)),
                ('product_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comment', to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
    ]