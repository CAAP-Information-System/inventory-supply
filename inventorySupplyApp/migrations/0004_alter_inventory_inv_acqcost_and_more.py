# Generated by Django 4.2.4 on 2023-09-13 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorySupplyApp', '0003_alter_inventory_inv_acqcost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inv_acqCost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='inv_acqDate',
            field=models.DateField(null=True),
        ),
    ]
