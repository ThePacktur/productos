# Generated by Django 3.2 on 2024-11-03 23:53

from django.db import migrations, models
import django.db.models.deletion
import productoApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('idDistribuidor', models.AutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('ciudad', models.CharField(max_length=15)),
                ('fechaDespacho', models.DateField()),
                ('fechaRecepcion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('idFactura', models.AutoField(primary_key=True, serialize=False)),
                ('fechaFacturacion', models.DateField()),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=15, validators=[productoApp.models.validacion_positivo])),
                ('iva', models.DecimalField(decimal_places=2, max_digits=5, validators=[productoApp.models.validacion_positivo])),
                ('descuentoTotal', models.DecimalField(decimal_places=2, max_digits=15, validators=[productoApp.models.validacion_positivo])),
                ('totalApagar', models.DecimalField(decimal_places=2, max_digits=15, validators=[productoApp.models.validacion_positivo])),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('denominacionOrigen', models.CharField(max_length=50)),
                ('cantidadProducto', models.IntegerField(validators=[productoApp.models.validacion_positivo])),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoApp.distribuidor')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productoApp.factura')),
            ],
        ),
    ]
