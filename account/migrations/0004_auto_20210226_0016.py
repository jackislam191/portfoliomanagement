# Generated by Django 3.1.5 on 2021-02-25 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210205_0036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Accounts', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]