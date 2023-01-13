from django.db import models
from django.contrib.auth.models import User


#User._meta.get_field('email').blank = False
User._meta.get_field('first_name').blank = False


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True, verbose_name = 'Город')
    street = models.CharField(max_length=50, blank=True, 
                              verbose_name = 'Улица')
    house = models.CharField(max_length=20, blank=True, verbose_name = 'Дом')
    number_phone = models.CharField(max_length=20, blank=False, 
                                    verbose_name = 'Телефон')
    comments = models.CharField(max_length=100, blank=True, 
                                verbose_name = 'Комментарии к заказу')
    
    def __str__(self):
        return f'{self.user} profile'