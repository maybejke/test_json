from django.db import models


# Create your models here.

class Dictionary(models.Model):
    ids = models.FloatField('id', unique=True)
    dim_name = models.CharField('Название категории', max_length=256)
    ident = models.SlugField('Индекфикационный номер', unique=True)
    is_ind = models.FloatField('Активно', default=0.0)


class Products_APK(models.Model):
    ids = models.FloatField('id', unique=True)
    parent_id = models.FloatField()
    name = models.CharField('Название', max_length=512)
    n_order = models.FloatField()
    methodology = models.CharField('Методология', max_length=256, blank=True)
    ei = models.CharField(blank=True, max_length=128)
    dictionary = models.ForeignKey(Dictionary, related_name='dictionary', null=True,
                                   on_delete=models.SET_NULL)


class Order(models.Model):
    """
    Легенда данных:
    "R_N_U_M": 2440.0, Номер строки данных
    "DIM_2954": 2.0, Показатели
    "DIM_369": 6.0, Вид представления
    "IS_CALC": 1.0,
    "DIM_2927": 28.0, Страны (код страны)
 -> "DIM_2955": 3.0, Направление перемещения (2 – импорт, 3 - экспорт)
    "DIM_2956": null, Товары АПК
    "DIM_2957": null, Промышленные товары
    "DIM_2958": null, Виды товаров Промышленность
 -> "DIM_2959": 25.0, Виды товаров АПК (соответствует id по словарю товаров АПК)
    "DDATE": 20160000001.0,
    "DT": "01.01.2016 12:00:00", Начало периода
    "DL": 1.0, Период (1 – год)
    "ID_IND": 2.0,
 -> "VL": "0.0" Значение в $США
    """
    r_n_u_m = models.FloatField('Номер строки данных')
    indicators = models.FloatField('Показатели - DIM_2954')
    view_type = models.FloatField('Вид представления "DIM_369"')
    is_calc = models.FloatField('Возможность посчитать?')
    country = models.FloatField('Страна')
    direction_of_travel = models.FloatField('Направление перемещений - DIM_2955')
    goods_apk = models.FloatField(blank=True)
    goods_industrial = models.FloatField(blank=True)
    type_of_goods_industrial = models.FloatField(blank=True)
    type_of_goods_apk = models.ForeignKey(Products_APK, related_name='product_apk', null=True,
                                          on_delete=models.SET_NULL)
    ddate = models.FloatField(null=True, blank=True)
    dt = models.DateTimeField()
    dl = models.FloatField()
    id_ind = models.FloatField(null=True, blank=True)
    vl = models.FloatField('Значение в долларах США')
