# Generated by Django 4.0.1 on 2022-02-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_rename_name_ideogramm_romanji_ideogramm_id_type_ideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ideogramm',
            name='Name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]