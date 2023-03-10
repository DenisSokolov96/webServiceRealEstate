from django.db import models


class Sellers(models.Model):
    id = models.AutoField('id', primary_key=True)
    fio = models.CharField('ФИО', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)
    id_district = models.IntegerField('Район')
    number_floors = models.IntegerField('Количество этажей')
    number_sell_floor = models.IntegerField('номер этажа')
    area = models.FloatField('Площадь')
    price = models.FloatField('Цена')

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавецы'

    def get_absolute_url(selfs):
        return f'/sellers/{selfs.id}'


class Buyers(models.Model):
    id = models.AutoField('id', primary_key=True)
    fio = models.CharField('ФИО', max_length=50)
    phone = models.CharField('Номер телефона', max_length=12)
    id_district = models.IntegerField('Район')
    min_area = models.FloatField('Площадь')
    max_area = models.FloatField('Площадь')
    price = models.FloatField('Цена')
    spicial_condition = models.BooleanField('Специальное условие')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def get_absolute_url(selfs):
        return f'/buyers/{selfs.id}'


class Directory(models.Model):
    id = models.AutoField('id', primary_key=True)
    name_district = models.CharField('Район', max_length=60)

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
