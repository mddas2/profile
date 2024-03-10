# Generated by Django 4.1 on 2024-03-10 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('slug', models.CharField(blank=True, max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('company_name', models.CharField(max_length=200)),
                ('company_slug', models.CharField(max_length=200, unique=True)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('company_logo', models.ImageField(upload_to='company/images')),
                ('description', models.TextField(blank=True, null=True)),
                ('company_size', models.CharField(max_length=350)),
                ('website', models.URLField(max_length=300, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company', to=settings.AUTH_USER_MODEL)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='company.companytype')),
            ],
        ),
    ]
