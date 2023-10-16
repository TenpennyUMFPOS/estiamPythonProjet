# Generated by Django 4.2.6 on 2023-10-16 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filmApi', '0001_initial'),
        ('customerApi', '0002_rename_name_customersmodel_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='rentalRecordModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentaldate', models.DateField()),
                ('returndate', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customerApi.customersmodel')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmApi.filmsmodel')),
            ],
        ),
    ]
