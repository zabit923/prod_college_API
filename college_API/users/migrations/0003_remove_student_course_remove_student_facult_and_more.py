# Generated by Django 5.0.1 on 2024-01-14 19:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_podgroup_remove_group_name_group_course_group_facult_and_more'),
        ('users', '0002_rename_courses_teacher_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='facult',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='course',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='facult',
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_group', to='data.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='group',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='teacher',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teacher',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_group', to='data.group'),
        ),
    ]
