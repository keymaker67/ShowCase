# Generated by Django 4.2 on 2024-02-27 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediamodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Medias', to='shop.productmodel', verbose_name='product'),
        ),
    ]
