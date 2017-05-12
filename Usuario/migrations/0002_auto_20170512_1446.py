# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 14:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid', models.CharField(max_length=11)),
                ('status', models.IntegerField(choices=[(1, 'ATIVO'), (0, 'BLOQUEADO')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CartaoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField(default=datetime.datetime.now)),
                ('data_fim', models.DateField(blank=True, null=True)),
                ('cartao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Cartao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuario.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='conta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Usuario.Conta'),
            preserve_default=False,
        ),
    ]