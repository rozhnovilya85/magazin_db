from django.db import models

# Create your models here.


class Street(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название улицы')
    city = models.ManyToManyField('City')

    def __str__(self):
        return self.name

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Улица'  # Надпись в единственном числе
        verbose_name_plural = 'Улицы'  # Надпись во множественном числе
        ordering = ['name']  # Сортировка полей (по возрастанию)


class City(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название города')

    def __str__(self):
        return self.name

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Город'  # Надпись в единственном числе
        verbose_name_plural = 'Города'  # Надпись во множественном числе
        ordering = ['name']  # Сортировка полей (по возрастанию)


class Magazine(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название магазина')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    street = models.ForeignKey(Street, on_delete=models.PROTECT, verbose_name='Улица')
    house = models.IntegerField(verbose_name='Номер дома')
    time_open = models.TimeField(verbose_name='Время открытия')
    time_close = models.TimeField(verbose_name='Время закрытия')

    def __str__(self):
        return self.name

    class Meta:  # Класс для названий нашей модели в админке
        verbose_name = 'Магазин'  # Надпись в единственном числе
        verbose_name_plural = 'Магазины'  # Надпись во множественном числе
        ordering = ['name']  # Сортировка полей (по возрастанию)




