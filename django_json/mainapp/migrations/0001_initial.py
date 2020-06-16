# Generated by Django 3.0.7 on 2020-06-16 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.FloatField(unique=True, verbose_name='id')),
                ('dim_name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('ident', models.SlugField(unique=True, verbose_name='Индекфикационный номер')),
                ('is_ind', models.FloatField(default=0.0, verbose_name='Активно')),
            ],
        ),
        migrations.CreateModel(
            name='Products_APK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.FloatField(unique=True, verbose_name='id')),
                ('parent_id', models.FloatField()),
                ('name', models.CharField(max_length=512, verbose_name='Название')),
                ('n_order', models.FloatField()),
                ('methodology', models.CharField(blank=True, max_length=256, verbose_name='Методология')),
                ('ei', models.CharField(blank=True, max_length=128)),
                ('dictionary', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dictionary', to='mainapp.Dictionary')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_n_u_m', models.FloatField(verbose_name='Номер строки данных')),
                ('indicators', models.FloatField(verbose_name='Показатели - DIM_2954')),
                ('view_type', models.FloatField(verbose_name='Вид представления "DIM_369"')),
                ('is_calc', models.FloatField(verbose_name='Возможность посчитать?')),
                ('country', models.FloatField(verbose_name='Страна')),
                ('direction_of_travel', models.FloatField(verbose_name='Направление перемещений - DIM_2955')),
                ('goods_apk', models.FloatField(blank=True)),
                ('goods_industrial', models.FloatField(blank=True)),
                ('type_of_goods_industrial', models.FloatField(blank=True)),
                ('ddate', models.FloatField(blank=True, null=True)),
                ('dt', models.DateTimeField()),
                ('dl', models.FloatField()),
                ('id_ind', models.FloatField(blank=True, null=True)),
                ('vl', models.FloatField(verbose_name='Значение в долларах США')),
                ('type_of_goods_apk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_apk', to='mainapp.Products_APK')),
            ],
        ),
    ]
