# Generated by Django 4.0.4 on 2022-05-09 12:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=8)),
                ('nom', models.CharField(max_length=30)),
                ('cognom', models.CharField(max_length=30)),
                ('DataNaix', models.DateField()),
                ('Telefon', models.CharField(max_length=9)),
                ('direccio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.personatemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumFederacio', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999999999)])),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.personatemplate')),
            ],
        ),
        migrations.CreateModel(
            name='compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IBAN', models.CharField(max_length=34)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.personatemplate')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PagementDomiciliat', models.BooleanField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.personatemplate')),
            ],
        ),
    ]
