# Generated by Django 5.1.3 on 2024-12-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vege", "0012_remove_recipe_is_deleted_remove_student_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
