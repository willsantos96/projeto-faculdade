# Generated by Django 4.2.4 on 2023-09-03 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contaescola'),
    ]

    operations = [
        migrations.AddField(
            model_name='contaescola',
            name='last_login',
            field=models.DateTimeField(blank=True, help_text='Data e hora do último login.', null=True, verbose_name='last login'),
        ),
    ]
