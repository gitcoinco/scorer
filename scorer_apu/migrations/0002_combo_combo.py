# Generated by Django 4.1.1 on 2022-10-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scorer_apu", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="combo",
            name="combo",
            field=models.JSONField(blank=True, db_index=True, default=list, null=True),
        ),
    ]