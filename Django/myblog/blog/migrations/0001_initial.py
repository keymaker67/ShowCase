# Generated by Django 4.2 on 2024-04-25 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100, verbose_name='Article Title')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, verbose_name='Slug')),
                ('body', models.TextField(verbose_name='Article Body')),
                ('thumb', models.ImageField(blank=True, default='default.png', null=True, upload_to='', verbose_name='Thumbnail')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='article_models', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
