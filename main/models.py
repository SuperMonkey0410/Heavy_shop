from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    """Модель товара"""

    AVAILABLE_CHOICES = (
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии')
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    size = models.ManyToManyField(to='Size', blank=True, verbose_name='Размер')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    image = models.ImageField(upload_to='media/main_product_image', verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Скидка (%)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    slug = models.SlugField(unique=True, verbose_name='URL')
    available = models.CharField(max_length=50, choices=AVAILABLE_CHOICES, default='in_stock', verbose_name='Наличие')

    # brand = models.CharField(max_length=100, blank=True, verbose_name='Бренд')

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})

    def get_discounted_price(self):
        """Возвращает цену со скидкой"""
        if self.discount:
            discount_amount = (self.discount / 100) * self.price
            return self.price - discount_amount
        return self.price

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Size(models.Model):
    """Модель размера одежда"""
    SIZE_CHOICES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )

    size = models.CharField(max_length=10, choices=SIZE_CHOICES, verbose_name='Размер')

    def __str__(self):
        return self.size

    class Meta:
        ordering = ['size']
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Category(models.Model):
    """Модель категории"""
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(unique=True, verbose_name='URL')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories',
                               verbose_name='Родительская категория')  # Категория в категориях (Обувь ---> Кроссовки;туфли)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ProductImage(models.Model):
    """"Модель для множественных изображений товара"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='media/product_images', verbose_name='Изображение')

    def __str__(self):
        return f"Image for {self.product.title}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


