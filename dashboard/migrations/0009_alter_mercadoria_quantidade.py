# Generated by Django 4.2.3 on 2023-08-03 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_alter_mercadoria_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercadoria',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
