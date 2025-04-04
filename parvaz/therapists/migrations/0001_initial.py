# Generated by Django 5.0.13 on 2025-03-25 17:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(blank=True, max_length=100)),
                ('years_of_experience', models.PositiveIntegerField(default=0)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('work_email', models.EmailField(blank=True, max_length=254)),
                ('office_address', models.TextField(blank=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_date', models.DateTimeField(blank=True, null=True)),
                ('speciality', models.ManyToManyField(related_name='therapists', to='therapists.speciality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='therapist_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
