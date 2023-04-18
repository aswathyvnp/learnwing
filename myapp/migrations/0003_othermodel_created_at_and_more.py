# Generated by Django 4.1.7 on 2023-04-04 12:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_othermodel_desig_remove_othermodel_empid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='othermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='othermodel',
            name='forget_password_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]