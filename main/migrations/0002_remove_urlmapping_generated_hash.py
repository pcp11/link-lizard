# Generated by Django 3.0.5 on 2020-06-04 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urlmapping',
            name='generated_hash',
        ),
    ]
