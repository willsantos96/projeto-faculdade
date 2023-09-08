# Generated by Django 4.2.4 on 2023-08-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_aluno_delete_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaEscola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password_hash', models.CharField(max_length=128)),
            ],
        ),
    ]