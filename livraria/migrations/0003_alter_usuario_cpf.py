# Generated by Django 4.1.7 on 2023-03-30 15:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0002_livro_capa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="cpf",
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]