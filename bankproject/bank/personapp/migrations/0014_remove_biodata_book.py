# Generated by Django 3.2.15 on 2022-08-27 17:12

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personapp', '0013_auto_20220827_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biodata',
            name='book',
        ),
    ]
