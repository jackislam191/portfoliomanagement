# Generated by Django 3.1.5 on 2021-02-04 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date joined'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='lamszeto2@gmail.com', max_length=60, unique=True, verbose_name='email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(default='A7cd237f', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='admin', max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
