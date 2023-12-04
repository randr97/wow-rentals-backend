# Generated by Django 3.2.23 on 2023-12-04 01:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0002_alter_officelocation_address_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='customer_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_bookings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dropoff_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dropoff_bookings', to='vehicle.officelocation'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pickup_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pickup_bookings', to='vehicle.officelocation'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='vehicle_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_bookings', to='vehicle.vehicle'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='class_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehicleclass'),
        ),
    ]
