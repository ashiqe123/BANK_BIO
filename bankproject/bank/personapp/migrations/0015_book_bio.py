# Generated by Django 3.2.15 on 2022-08-27 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('personapp', '0014_remove_biodata_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bio',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='personapp.biodata'),
        ),
    ]
