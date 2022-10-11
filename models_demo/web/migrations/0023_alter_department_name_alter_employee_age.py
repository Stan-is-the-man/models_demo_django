# Generated by Django 4.1.2 on 2022-10-10 12:34

from django.db import migrations, models
import models_demo.web.validators


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0022_alter_employee_age_alter_employee_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.PositiveIntegerField(default=0, validators=[models_demo.web.validators.validate_over_18_years_old]),
        ),
    ]