# Generated by Django 4.2.2 on 2023-06-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
