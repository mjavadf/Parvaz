# Generated by Django 5.2.4 on 2025-07-08 14:01

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_clientprofile_languages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientprofile',
            name='country_of_origin',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='clientprofile',
            name='country_of_residence',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='therapistprofile',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
    ]
