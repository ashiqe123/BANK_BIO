# Generated by Django 3.2.15 on 2022-08-27 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personapp', '0019_auto_20220827_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='biodata',
            name='account',
        ),
        migrations.AlterField(
            model_name='biodata',
            name='name',
            field=models.CharField(max_length=124),
        ),
        migrations.AlterField(
            model_name='biodata',
            name='type',
            field=models.CharField(blank=True, choices=[('SAVINGS ACCOUNT', 'SAVINGS ACCOUNT'), ('CURRENT ACCOUNT', 'CURRENT ACCOUNT'), ('NRI ACCOUNT', 'NRI ACCOUNT')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='account',
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personapp.country'),
        ),
        migrations.AddField(
            model_name='biodata',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personapp.city'),
        ),
        migrations.AddField(
            model_name='biodata',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='personapp.country'),
        ),
    ]
