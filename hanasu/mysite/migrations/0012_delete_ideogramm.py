# Generated by Django 4.0.1 on 2022-02-01 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_rename_romaji_ideogramm_romanji'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ideogramm',
        ),
    ]
