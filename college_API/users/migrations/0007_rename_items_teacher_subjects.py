# Generated by Django 5.0.1 on 2024-01-15 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_teacher_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='items',
            new_name='subjects',
        ),
    ]
