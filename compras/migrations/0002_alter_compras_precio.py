# Generated by Django 4.2.5 on 2023-09-23 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
