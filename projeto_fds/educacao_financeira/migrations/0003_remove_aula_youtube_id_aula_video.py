# Generated by Django 5.1.1 on 2024-10-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("educacao_financeira", "0002_resumo_usuario"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="aula",
            name="youtube_id",
        ),
        migrations.AddField(
            model_name="aula",
            name="video",
            field=models.FileField(blank=True, null=True, upload_to="videos/"),
        ),
    ]
