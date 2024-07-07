# Generated by Django 4.2 on 2024-03-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilemodel',
            name='public',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Public'),
        ),
        migrations.AlterField(
            model_name='userrelationmodel',
            name='relation_type',
            field=models.CharField(choices=[('follower', 'Follower'), ('blocked', 'Blocked')], max_length=15, verbose_name='Relation type'),
        ),
    ]