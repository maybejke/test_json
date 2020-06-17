# Generated by Django 3.0.7 on 2020-06-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='dictionary',
        ),
        migrations.AlterField(
            model_name='order',
            name='goods_apk',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='goods_industrial',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='type_of_goods_industrial',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
