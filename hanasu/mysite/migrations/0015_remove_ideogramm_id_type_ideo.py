# Generated by Django 4.0.1 on 2022-02-01 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0014_alter_ideogramm_img_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ideogramm',
            name='id_type_ideo',
        ),
    ]