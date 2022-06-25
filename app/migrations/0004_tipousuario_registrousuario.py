# Generated by Django 4.0.4 on 2022-05-15 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_productos_carrito_alter_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'db_tipo_usuario',
            },
        ),
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('alias_usuario', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=20)),
                ('apellido_usuario', models.CharField(max_length=20)),
                ('correo_usuario', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('repetir_password', models.CharField(max_length=20)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipousuario')),
            ],
            options={
                'db_table': 'db_registro_usuario',
            },
        ),
    ]