# Generated by Django 4.2.4 on 2023-09-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_contaescola_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='contaescola',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]