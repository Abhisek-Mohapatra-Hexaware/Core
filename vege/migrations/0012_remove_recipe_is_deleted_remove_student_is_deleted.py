# Generated by Django 5.1.3 on 2024-12-05 15:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0011_student_is_deleted"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="is_deleted",
        ),
        migrations.RemoveField(
            model_name="student",
            name="is_deleted",
        ),
    ]
