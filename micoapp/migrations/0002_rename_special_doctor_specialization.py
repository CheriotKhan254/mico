# Generated by Django 5.1.3 on 2024-12-06 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('micoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='special',
            new_name='specialization',
        ),
    ]
