# Generated by Django 5.1.4 on 2025-02-09 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_remove_order_movie_order_movies_order_user_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(default="0001-01-01"),
            preserve_default=False,
        ),
    ]
