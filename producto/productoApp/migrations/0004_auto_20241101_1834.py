# Generated by Django 3.2 on 2024-11-01 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productoApp', '0003_alter_productos_idproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribuidor',
            name='idDistribuidor',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='factura',
            name='idFactura',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
