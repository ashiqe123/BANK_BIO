# Generated by Django 3.2.15 on 2022-08-28 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0023_auto_20220828_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DOB',
            field=models.DateField(verbose_name='DOB(dd/mm/yy)'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=True),
        ),
    ]
