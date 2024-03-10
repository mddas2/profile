# Generated by Django 4.1 on 2024-03-10 14:00

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('phone', models.CharField(default='', max_length=15, null=True, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('country', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('remarks', models.CharField(default='', max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='profiles/images')),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'SUPER_ADMIN'), (2, 'ADMIN'), (3, 'ENTREPRENEUR'), (5, 'EMPLOYER')], null=True)),
                ('old_password_change_case', models.BooleanField(default=True)),
                ('provider', models.PositiveSmallIntegerField(choices=[(1, 'system'), (2, 'google'), (3, 'facebook')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
