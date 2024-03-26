# Generated by Django 5.0.1 on 2024-03-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0009_delete_cart"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("v_name", models.CharField(max_length=255)),
                ("v_video", models.FileField(upload_to="videos")),
            ],
        ),
        migrations.DeleteModel(
            name="Product",
        ),
    ]
