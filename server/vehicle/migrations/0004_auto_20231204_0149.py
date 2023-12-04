# Generated by Django 3.2.23 on 2023-12-04 01:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0003_auto_20231204_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='coupon_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_coupons', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='next_available_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
