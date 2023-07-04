# Generated by Django 4.0.2 on 2023-06-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phon_number', models.BigIntegerField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('salary', models.PositiveIntegerField()),
                ('penalty_fee', models.PositiveIntegerField()),
            ],
        ),
    ]
