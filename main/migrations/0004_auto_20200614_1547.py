# Generated by Django 3.0.7 on 2020-06-14 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200614_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmapping',
            name='original_url',
            field=models.TextField(validators=[django.core.validators.URLValidator]),
        ),
    ]
