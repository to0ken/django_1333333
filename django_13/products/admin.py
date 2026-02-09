from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    # пути
    slug= models.SlugField(max_length=100, verbose_name='URL')

    class Meta():
        ordering = ('name',)
        verbose_name = 'Категорию'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_list_by_category', args=[self.slug])
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(max_length=200, verbose_name='URL')
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='в наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    

    class Meta():
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id, self.slug])

class Discount(models.Model):
    DISCOUNT_TYPES = [
        ('percentage', '%'),
        ('fixed', 'Рубли'),
    ]

    APPLY_TO = [
        ('all', 'На весь заказ'),
        ('category', 'На категорию'),
        ('product', 'На товар'),
    ]

    name = models.CharField('Название', max_length=100)
    discount_type = models.CharField('Тип', max_length=20, choices=DISCOUNT_TYPES, default='percentage')
    value = models.DecimalField('Значение', max_digits=10, decimal_places=2)
    apply_to = models.CharField('Для', max_length=20, choices=APPLY_TO, default='product')
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Категория')
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Товар')
    code = models.CharField('Промокод', max_length=50, blank=True, null=True)
    start_date = models.DateTimeField('Начало', default=timezone.now)
    end_date = models.DateTimeField('Конец', default=timezone.now)
    active = models.BooleanField('Вкл', default=True)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f"{self.name} ({self.value}{'%' if self.discount_type == 'percentage' else '₽'})"





