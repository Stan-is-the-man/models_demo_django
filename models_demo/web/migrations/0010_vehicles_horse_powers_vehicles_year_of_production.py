# Generated by Django 4.1.2 on 2022-10-06 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_employee_own_vehicles'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='horse_powers',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='year_of_production',
            field=models.DateField(null=True),
        ),
    ]