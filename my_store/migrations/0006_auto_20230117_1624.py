# Generated by Django 4.1.5 on 2023-01-17 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("my_store", "0005_remove_customer_store_custo_last_na_e6a359_idx_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO my_store_collection (title) VALUES ('collection1')
            """,
            """
            DELETE FROM  my_store_collection WHERE title = 'collection1'
            """,
        )
    ]
