from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('classperiod', '0001_initial'),  # Make sure this points to your last successful migration
    ]

    operations = [
        migrations.RunSQL(
            sql=[
                # Ensure start_time and end_time are timestamp with time zone
                "ALTER TABLE classperiod_classperiod ALTER COLUMN start_time TYPE timestamp with time zone",
                "ALTER TABLE classperiod_classperiod ALTER COLUMN end_time TYPE timestamp with time zone",
            ],
            reverse_sql=[
                # If needed, convert back to time without time zone
                "ALTER TABLE classperiod_classperiod ALTER COLUMN start_time TYPE time without time zone USING start_time::time",
                "ALTER TABLE classperiod_classperiod ALTER COLUMN end_time TYPE time without time zone USING end_time::time",
            ]
        ),
    ]