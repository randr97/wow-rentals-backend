# Generated by Django 3.2.23 on 2023-12-10 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_alter_booking_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('goods_and_services_tax', models.FloatField()),
                ('total', models.FloatField()),
                ('bill_to_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill_to_invoices', to='vehicle.officelocation')),
                ('dropoff_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dropoff_loc_invoices', to='vehicle.officelocation')),
                ('ship_to_address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ship_to_invoices', to='vehicle.officelocation')),
            ],
        ),
    ]
