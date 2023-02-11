from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(verbose_name='پرداخت شده / نشده')
    payment_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران'

    def __str__(self):
        return self.owner.get_full_name()

    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def get_detail_sum(self):
        return self.count * self.price

    class Meta:
        verbose_name = 'جزییات محصول'
        verbose_name_plural = 'اطلاعات جزییات محصولات'

    def __str__(self):
        return self.product.title


class UserAddress(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    city = models.CharField(max_length=100, verbose_name='شهر')
    street = models.CharField(max_length=500, verbose_name='خیابان')
    alley = models.CharField(max_length=200, verbose_name='کوچه')
    number = models.IntegerField(verbose_name='پلاک')
    unit = models.IntegerField(verbose_name='واحد')
    mobile = models.IntegerField(verbose_name='تلفن')

    class Meta:
        verbose_name = 'آدرس خریدار'
        verbose_name_plural = 'آدرس خریداران'

    def __str__(self):
        return self.owner.get_full_name()


