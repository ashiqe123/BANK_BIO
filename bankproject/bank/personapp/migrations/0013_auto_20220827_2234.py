# Generated by Django 3.2.15 on 2022-08-27 17:04

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personapp', '0012_auto_20220827_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='book',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='personapp.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BANK PASS BOOK', 'BANK PASS BOOK'), ('CREDIT CARD', 'CREDIT CARD'), ('DEBIT CARD', 'DEBIT CARD'), ('CHECKBOOK', 'CHECKBOOK')], max_length=47),
        ),
    ]