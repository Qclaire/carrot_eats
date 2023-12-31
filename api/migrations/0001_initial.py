# Generated by Django 4.2.2 on 2023-06-24 17:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(2)],
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254,
                        unique=True,
                        validators=[django.core.validators.EmailValidator()],
                    ),
                ),
                (
                    "password",
                    models.CharField(
                        max_length=255,
                        validators=[django.core.validators.MinLengthValidator(8)],
                    ),
                ),
                ("role", models.CharField(max_length=50)),
            ],
        ),
    ]
