# Generated by Django 5.1 on 2024-08-11 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]