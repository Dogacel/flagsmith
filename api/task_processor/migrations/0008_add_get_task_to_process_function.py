# Generated by Django 3.2.18 on 2023-04-20 02:45

from django.db import migrations

from core.migration_helpers import PostgresOnlyRunSQL
import os


class Migration(migrations.Migration):
    dependencies = [
        ("task_processor", "0007_add_is_locked"),
    ]

    operations = [
        PostgresOnlyRunSQL.from_sql_file(
            os.path.join(
                os.path.dirname(__file__),
                "sql",
                "0008_get_tasks_to_process.sql",
            ),
            reverse_sql="DROP FUNCTION IF EXISTS get_tasks_to_process",
        ),
        PostgresOnlyRunSQL.from_sql_file(
            os.path.join(
                os.path.dirname(__file__),
                "sql",
                "0008_get_recurring_tasks_to_process.sql",
            ),
            reverse_sql="DROP FUNCTION IF EXISTS get_recurringtasks_to_process",
        ),
    ]
