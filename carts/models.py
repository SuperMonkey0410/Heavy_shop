from django.db import models
from main.models import Product
from users.models import User



class CartQueryset(models.QuerySet):
    """Переопределение QuerySet manager для модели Cart"""
    def total_quantity(self):
        return sum(cart.quantity for cart in self)

    def total_price(self):
        return sum(cart.products_price() for cart in self)

class Cart(models.Model):
    """Корзина"""
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Пользователь')
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=32, blank=True, null=True, verbose_name='Ключ сессии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    objects = CartQueryset.as_manager()

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина {self.user.username} | Товар {self.product.title} | Количество {self.quantity}'

    def products_price(self):
        return round(self.product.get_discounted_price() * self.quantity, 2)


class CartItems:
    """Товары корзины"""
