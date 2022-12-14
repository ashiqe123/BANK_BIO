# Generated by Django 3.2.15 on 2022-08-27 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('personapp', '0011_auto_20220826_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('BANK PASS BOOK', 'BANK PASS BOOK'), ('CREDIT CARD', 'CREDIT CARD'), ('DEBIT CARD', 'DEBIT CARD'), ('CHECKBOOK', 'CHECKBOOK')], max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='biodata',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personapp.account'),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
