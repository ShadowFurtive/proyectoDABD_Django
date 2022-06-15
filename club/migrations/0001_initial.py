# Generated by Django 4.0.4 on 2022-06-10 14:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('IBAN', models.CharField(max_length=34, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Horari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PersonaTemplate',
            fields=[
                ('DNI', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=30)),
                ('cognom', models.CharField(max_length=30)),
                ('DataNaix', models.DateField()),
                ('Telefon', models.CharField(max_length=9)),
                ('direccio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('tmpl_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='club.personatemplate')),
                ('PagementDomiciliat', models.BooleanField()),
            ],
            bases=('club.personatemplate',),
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('tmpl_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='club.personatemplate')),
                ('numFederacio', models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999999)])),
                ('compteIBAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.compte')),
            ],
            bases=('club.personatemplate',),
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modalitat', models.PositiveSmallIntegerField(choices=[(1, 'Boxa'), (2, 'Thai'), (3, 'MMA')])),
                ('tipus', models.PositiveSmallIntegerField(choices=[(1, 'Físic'), (2, 'Técnic'), (3, 'Contacte')])),
                ('realitzada', models.BooleanField(default=False)),
                ('horari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.horari')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.entrenador')),
            ],
            options={
                'unique_together': {('horari', 'coach')},
            },
        ),
        migrations.CreateModel(
            name='SolicitudFederacio',
            fields=[
                ('numero', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pagament', models.BooleanField()),
                ('concedida', models.BooleanField()),
                ('data', models.DateField()),
                ('numFederacio', models.BigIntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(99999999999999)])),
                ('dataCaducitat', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.client')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('tmpl_persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='club.personatemplate')),
                ('compteIBAN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.compte')),
            ],
            bases=('club.personatemplate',),
        ),
        migrations.CreateModel(
            name='Inscripcio',
            fields=[
                ('numInscripcio', models.BigIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999999999999)])),
                ('tipus', models.PositiveSmallIntegerField(choices=[(1, 'Complet'), (2, 'Fitness'), (3, 'Matins')])),
                ('dataInscripcio', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.client')),
            ],
        ),
        migrations.AddField(
            model_name='horari',
            name='entrenadores',
            field=models.ManyToManyField(through='club.Classe', to='club.entrenador'),
        ),
        migrations.CreateModel(
            name='HistoricPagaments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('Pagament', models.IntegerField()),
                ('numInscripcio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.inscripcio')),
            ],
            options={
                'unique_together': {('numInscripcio', 'data')},
            },
        ),
        migrations.AddField(
            model_name='client',
            name='classes',
            field=models.ManyToManyField(blank=True, to='club.classe'),
        ),
        migrations.AddField(
            model_name='client',
            name='compteIBAN',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.compte'),
        ),
        migrations.AlterUniqueTogether(
            name='horari',
            unique_together={('horario', 'data')},
        ),
        migrations.CreateModel(
            name='Faltes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataFalta', models.DateField()),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.personal')),
            ],
            options={
                'unique_together': {('dataFalta', 'personal')},
            },
        ),
    ]
