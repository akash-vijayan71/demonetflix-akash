# Generated by Django 5.0.1 on 2024-02-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_remove_cart_cp_total_cart_cp_amount_cart_cp_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("odr_name", models.CharField(max_length=255)),
                ("odr_qty", models.IntegerField()),
                ("odr_price", models.FloatField()),
                ("odr_image", models.FileField(upload_to="")),
                ("odr_amount", models.FloatField()),
            ],
        ),
    ]
