# Generated by Django 4.0.10 on 2024-05-19 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_datospersonales_apellidos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='nombre',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombres'),
        ),
    ]