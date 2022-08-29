# Generated by Django 3.2.15 on 2022-08-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('DOB', models.DateField()),
                ('age', models.IntegerField(max_length=10)),
                ('gender', models.CharField(max_length=25)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('email_id', models.EmailField(max_length=254)),
                ('adress', models.TextField(max_length=500)),
            ],
        ),
    ]
