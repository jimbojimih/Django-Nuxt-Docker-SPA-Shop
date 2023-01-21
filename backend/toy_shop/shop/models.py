from django.db import models
from PIL import Image as PillowImage

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 verbose_name = 'Подкатегория')    
    name = models.CharField(max_length=100, verbose_name = 'Название')

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, 
                                     verbose_name = 'Подкатегория')
    name = models.CharField(max_length=100, verbose_name = 'Название')
    description = models.TextField(verbose_name = 'Описание') 
    price = models.DecimalField(max_digits=6, decimal_places=0, 
                                verbose_name = 'Цена')   
    available = models.BooleanField(default=True, verbose_name = 'Видимость')
    created = models.DateTimeField(auto_now_add=True, 
                                   verbose_name = 'Дата создания')
    updated = models.DateTimeField(auto_now_add=True, 
                                   verbose_name = 'Дата обновления')    

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', 
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
    
    def save(self):
        super().save()
        img = PillowImage.open(self.image.path)
        if img.height > 466 or img.width > 466:
            size = (466, 466)
            img.thumbnail(size)
            img.save(self.image.path)
        
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
