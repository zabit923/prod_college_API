# Generated by Django 5.0.1 on 2024-01-15 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
