# Generated by Django 4.0.4 on 2022-04-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0004_alter_transacao_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='descricao',
            field=models.CharField(max_length=200),
        ),
    ]
