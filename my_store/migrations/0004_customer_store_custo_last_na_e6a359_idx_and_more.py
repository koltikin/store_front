# Generated by Django 4.1.5 on 2023-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_store", "0003 _add_slug_to_product"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="customer",
            index=models.Index(
                fields=["last_name", "first_name"],
                name="store_custo_last_na_e6a359_idx",
            ),
        ),
        migrations.AlterModelTable(
            name="customer",
            table="store_customers",
        ),
    ]
