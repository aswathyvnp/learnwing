# Generated by Django 4.1.7 on 2023-04-04 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='othermodel',
            name='desig',
        ),
        migrations.RemoveField(
            model_name='othermodel',
            name='empid',
        ),
        migrations.AddField(
            model_name='othermodel',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
