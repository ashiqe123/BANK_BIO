# Generated by Django 3.2.15 on 2022-08-27 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0020_auto_20220827_2342'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='biodata',
            new_name='Person',
        ),
    ]
