# Generated by Django 4.2 on 2024-02-29 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previews', to='content.postmodel', verbose_name='Post')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previews', to='user.userprofile', verbose_name='Profile')),
                ('story', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previews', to='content.storymodel', verbose_name='Story')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Preview',
                'verbose_name_plural': 'Previews',
            },
        ),
    ]
