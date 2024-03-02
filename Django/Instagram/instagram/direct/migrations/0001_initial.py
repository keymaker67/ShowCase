# Generated by Django 4.2 on 2024-03-02 09:56

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
            name='DirectMessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('text_message', models.TextField(blank=True, verbose_name='Text message')),
                ('media_file', models.FileField(blank=True, upload_to='message/%Y/%m', verbose_name='Media File')),
                ('media_type', models.CharField(blank=True, choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio')], max_length=10, verbose_name='Media type')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver_direct_messages', to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender_direct_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender')),
            ],
            options={
                'verbose_name': 'Direct message',
                'verbose_name_plural': 'Direct messages',
            },
        ),
    ]
