# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-09-15 18:34
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import general.functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='parol')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='son dəfə daxil olub')),
                ('is_superuser', models.BooleanField(default=False, help_text='İstifadəçiyə bütün icazələri verir.', verbose_name='superistifadəçi statusu')),
                ('username', models.CharField(help_text='Tələb olunur. 75 simvol və ya az. Hərflər, Rəqəmlər və @/./+/-/_ simvollar.', max_length=100, unique=True, verbose_name='istifadəçi adı')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='ad')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='soyad')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='e-poçt ünvanı')),
                ('salary', models.DecimalField(decimal_places=2, default=0.0, max_digits=19, verbose_name='Maaş')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=general.functions.path_and_rename)),
                ('passport_picture1', models.ImageField(blank=True, null=True, upload_to=general.functions.path_and_rename)),
                ('passport_picture2', models.ImageField(blank=True, null=True, upload_to=general.functions.path_and_rename)),
                ('verified', models.BooleanField(default=False, verbose_name='Təstiqlənmə')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Telefonu')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('usertype', models.IntegerField(blank=True, choices=[(1, 'Admin'), (4, 'Adminstrativ'), (2, 'Employee'), (3, 'Customer')], null=True, verbose_name='User Type')),
                ('is_staff', models.BooleanField(default=False, help_text='İstifadəçinin admin panelinə daxil olub, olmayacağını təyin edir.', verbose_name='admin statusu')),
                ('is_active', models.BooleanField(default=True, help_text='İstifadəçinin aktiv və ya qeyri-aktiv olmasını təyin edir. Hesabları silmək əvəzinə bundan istifadə edin.', verbose_name='Aktiv')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='qoşulub')),
            ],
            options={
                'verbose_name': 'İstifadəçi',
                'verbose_name_plural': 'İstifadəçilər',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserConfrimationKeys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=255, null=True)),
                ('expired_date', models.DateTimeField()),
                ('expired', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Təstiqlənmiş user',
                'verbose_name_plural': 'Təstiqlənmiş userlər',
                'ordering': ('-date',),
            },
        ),
    ]
