# Generated by Django 4.0.1 on 2022-02-01 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_rename_romanji_ideogramm_romanji'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ideogramm',
            old_name='romanji',
            new_name='romaji',
        ),
    ]