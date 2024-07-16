# Generated by Django 5.0.7 on 2024-07-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=6)),
                ('id_number', models.IntegerField()),
                ('bio', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('place_of_work', models.CharField(max_length=35)),
                ('salary_earned', models.IntegerField()),
                ('level_of_education', models.CharField(max_length=30)),
            ],
        ),
    ]