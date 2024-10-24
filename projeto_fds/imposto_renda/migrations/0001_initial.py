# Generated by Django 5.1.1 on 2024-10-09 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImpostoRenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('renda_anual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imposto_calculado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_calculo', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
