# Generated by Django 5.0.1 on 2024-02-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0006_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cp_user",
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="odr_status",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="odr_user",
            field=models.CharField(max_length=255, null=True),
        ),
    ]