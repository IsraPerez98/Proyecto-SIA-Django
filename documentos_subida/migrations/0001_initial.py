# Generated by Django 3.0.2 on 2020-01-16 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import documentos_subida.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('codigo', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField(default=False)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_subida', models.DateField(auto_now=True)),
                ('archivo', models.FileField(unique=True, upload_to=documentos_subida.models.directorio_subida)),
                ('asignatura_principal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documentos_subida.Asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('descripcion', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EnlaceAsignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos_subida.Asignatura')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos_subida.Documento')),
            ],
        ),
        migrations.AddField(
            model_name='documento',
            name='semestre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='documentos_subida.Semestre'),
        ),
        migrations.AddField(
            model_name='documento',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='documentos_subida.Tipo'),
        ),
        migrations.AddField(
            model_name='documento',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]