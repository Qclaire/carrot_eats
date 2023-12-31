# Generated by Django 4.2.2 on 2023-06-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0014_role_id_alter_role_name_alter_role_table"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("RESTAURANT_MANAGER", "restaurant_manager"),
                    ("DELIVERY_AGENT", "delivery_agent"),
                    ("ADMIN", "admin"),
                    ("CUSTOMER", "customer"),
                ],
                default="customer",
                max_length=255,
            ),
        ),
    ]
