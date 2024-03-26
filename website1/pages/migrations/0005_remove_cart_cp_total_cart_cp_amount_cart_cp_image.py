# Generated by Django 5.0.1 on 2024-02-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0004_cart"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="cp_total",
        ),
        migrations.AddField(
            model_name="cart",
            name="cp_amount",
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name="cart",
            name="cp_image",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
