# Generated by Django 4.2 on 2023-05-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hosting", "0002_room_owner_alter_client_name_alter_room_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="duration",
            field=models.IntegerField(),
        ),
    ]
