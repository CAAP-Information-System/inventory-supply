# Generated by Django 4.2.5 on 2023-09-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorySupplyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inv_description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inv_model',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inv_property',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inv_serial',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]