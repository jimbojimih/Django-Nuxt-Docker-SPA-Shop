from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(User, related_name='items', 
                            on_delete=models.CASCADE, blank=True)
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True, 
                                      verbose_name='Дата создания')
    price = models.DecimalField(max_digits=6, decimal_places=0, 
                                verbose_name = 'Цена', null=True)
    name = models.CharField(max_length=100, verbose_name = 'Название', 
                            null=True)
    selled = models.BooleanField(default=False, verbose_name = 'Продано')

    class Meta:
        verbose_name = 'Товар в корзина'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return self.name

