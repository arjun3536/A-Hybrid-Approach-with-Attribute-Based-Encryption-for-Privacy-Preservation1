# Generated by Django 5.0.6 on 2024-05-12 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='courtcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseid', models.CharField(default='', max_length=200)),
                ('casetype', models.CharField(default='', max_length=200)),
                ('victimside', models.CharField(default='', max_length=200)),
                ('accuseside', models.CharField(default='', max_length=200)),
                ('casedate', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='operatorregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('dob', models.CharField(default='', max_length=200)),
                ('emailid', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('mobilenumber', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('gender', models.CharField(default='', max_length=200)),
                ('dob', models.CharField(default='', max_length=200)),
                ('emailid', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=200)),
                ('mobilenumber', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('windturbine', models.CharField(default='', max_length=500)),
                ('steamproduction', models.CharField(default='', max_length=500)),
                ('energyeffeciency', models.CharField(default='', max_length=500)),
                ('synchronousmotors', models.CharField(default='', max_length=500)),
                ('entrydate', models.CharField(default='', max_length=500)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='HYBRIDAPPROACHAPP.userregister')),
            ],
        ),
    ]
