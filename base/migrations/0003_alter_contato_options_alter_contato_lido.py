# Generated by Django 4.2.10 on 2024-02-16 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_reserva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contato',
            options={'ordering': ['-data', 'lido'], 'verbose_name': 'Formulário de Contato', 'verbose_name_plural': 'Formulários de Contato'},
        ),
        migrations.AlterField(
            model_name='contato',
            name='lido',
            field=models.BooleanField(default=True, verbose_name='Mensagem lida'),
        ),
    ]
