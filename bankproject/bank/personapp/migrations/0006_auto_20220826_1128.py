# Generated by Django 3.2.15 on 2022-08-26 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0005_auto_20220826_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='NRI_account',
            new_name='account',
        ),
        migrations.RemoveField(
            model_name='account',
            name='current_account',
        ),
        migrations.RemoveField(
            model_name='account',
            name='savings_account',
        ),
    ]
