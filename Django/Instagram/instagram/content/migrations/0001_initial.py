# Generated by Django 4.2 on 2024-03-02 01:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('allow_comments', models.BooleanField(blank=True, default=True, verbose_name='Allow comments')),
                ('close_friends_only', models.BooleanField(blank=True, default=False, verbose_name='Close friends only')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_stories', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Story',
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('allow_comments', models.BooleanField(blank=True, default=True, verbose_name='Allow comments')),
                ('show_like', models.BooleanField(blank=True, default=True, verbose_name='Show like')),
                ('close_friends_only', models.BooleanField(blank=True, default=False, verbose_name='Close friends only')),
                ('caption', models.CharField(blank=True, max_length=500, null=True, verbose_name='Caption')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='MentionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('object_id', models.PositiveSmallIntegerField(verbose_name='Object ID')),
                ('content_type', models.ForeignKey(limit_choices_to={'model__in': ['post', 'story']}, on_delete=django.db.models.deletion.PROTECT, related_name='mention', to='contenttypes.contenttype', verbose_name='Content type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mentioned_users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Mention',
                'verbose_name_plural': 'Mentions',
                'unique_together': {('content_type', 'object_id', 'user')},
            },
        ),
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('object_id', models.PositiveSmallIntegerField(verbose_name='Object ID')),
                ('media_file', models.FileField(upload_to='%Y/%m', verbose_name='Media File')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10)),
                ('content_type', models.ForeignKey(limit_choices_to={'model__in': ['post', 'story']}, on_delete=django.db.models.deletion.PROTECT, related_name='media', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Medias',
                'unique_together': {('content_type', 'object_id', 'media_file')},
            },
        ),
    ]
