# Generated by Django 5.1.1 on 2024-09-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanejamentoAposentadoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade_atual', models.IntegerField()),
                ('idade_aposentadoria', models.IntegerField()),
                ('meta_renda_aposentadoria', models.DecimalField(decimal_places=2, max_digits=10)),
                ('economia_mensal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
