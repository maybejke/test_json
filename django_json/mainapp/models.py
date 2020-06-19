from django.db import models


# Create your models here.

class Dictionary(models.Model):
    class Meta:
        verbose_name = 'Словаь'
        ordering = ('ids', )
    ids = models.FloatField('id', unique=True)
    dim_name = models.CharField('Название категории', max_length=256)
    ident = models.SlugField('Индекфикационный номер', unique=True)
    is_ind = models.FloatField('Активно', default=0.0)

    def __str__(self):
        return f'{self.dim_name} - {self.ident}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('ids', 'n_order')

    ids = models.FloatField('id', unique=True)
    parent_id = models.FloatField()
    name = models.CharField('Название', max_length=512)
    n_order = models.FloatField()
    methodology = models.CharField('Методология', max_length=256, blank=True)
    ei = models.CharField(blank=True, max_length=128)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    r_n_u_m = models.FloatField('Номер строки данных')
    indicators = models.FloatField('Показатели - DIM_2954')
    view_type = models.FloatField('Вид представления "DIM_369"')
    is_calc = models.FloatField('Возможность посчитать?')
    country = models.FloatField('Страна')
    direction_of_travel = models.FloatField('Направление перемещений - DIM_2955')
    goods_apk = models.FloatField(blank=True, null=True)
    goods_industrial = models.FloatField(blank=True, null=True)
    type_of_goods_industrial = models.FloatField(blank=True, null=True)
    type_of_goods_apk = models.ForeignKey(Product, related_name='product_apk', null=True,
                                          on_delete=models.SET_NULL)
    ddate = models.FloatField(null=True, blank=True)
    # dt = models.DateTimeField()
    dl = models.FloatField()
    id_ind = models.FloatField(null=True, blank=True)
    vl = models.FloatField('Значение в долларах США')

    def __str__(self):
        return f'Заказ - {self.id}'
