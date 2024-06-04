from django.db import models
from django.contrib.auth.models import User

from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
        
    def __str__(self):
        return f'Корзина, {self.user.username}'
