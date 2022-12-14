# Generated by Django 4.1.2 on 2022-10-06 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_accesscard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=15)),
                ('modification', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleAdmin',
            fields=[
                ('vehicles_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.vehicles')),
            ],
            bases=('web.vehicles',),
        ),
    ]
