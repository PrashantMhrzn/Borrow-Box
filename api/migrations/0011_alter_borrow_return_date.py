# Generated by Django 5.2.2 on 2025-06-21 09:58

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_borrow_return_date_alter_reserve_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateField(default=api.models.get_default_return_date),
        ),
    ]
