# Generated by Django 3.2.15 on 2022-08-27 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personapp', '0016_auto_20220827_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='book',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='personapp.book'),
        ),
    ]