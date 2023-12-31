# Generated by Django 4.0.2 on 2023-06-27 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_phon_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='penalty_fee',
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.PositiveIntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='penalties', to='employee.employee')),
            ],
        ),
    ]
