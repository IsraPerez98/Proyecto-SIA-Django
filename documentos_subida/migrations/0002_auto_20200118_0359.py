# Generated by Django 3.0.2 on 2020-01-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos_subida', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='fecha_subida',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
