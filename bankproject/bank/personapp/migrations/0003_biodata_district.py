# Generated by Django 3.2.15 on 2022-08-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personapp', '0002_alter_biodata_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='district',
            field=models.BooleanField(default=True),
        ),
    ]
