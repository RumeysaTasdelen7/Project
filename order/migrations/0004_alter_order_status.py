# Generated by Django 5.0.3 on 2024-03-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_order_address_alter_order_customer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("processing", "Processing"),
                    ("shipped", "Shipped"),
                    ("delivered", "Delivered"),
                    ("cancelled", "Cancelled"),
                    ("pending", "Pending"),
                ],
                default="processing",
                max_length=100,
            ),
        ),
    ]