# Generated by Django 3.2.23 on 2023-12-10 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='booking_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.booking'),
        ),
    ]