# Generated by Django 4.0.4 on 2022-05-13 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoCarrito',
        ),
        migrations.DeleteModel(
            name='TipoCliente',
        ),
    ]