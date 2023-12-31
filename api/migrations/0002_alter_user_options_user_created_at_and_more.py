# Generated by Django 4.2.2 on 2023-06-24 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "get_latest_by": "created_at",
                "ordering": ("-created_at", "-last_modified"),
            },
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="user",
            name="last_modified",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
