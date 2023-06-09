# Generated by Django 4.2 on 2023-04-05 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LearnwingApp', '0002_rename_course_name_course_course_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='course_title',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_desc',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_fee',
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_image',
        ),
        migrations.CreateModel(
            name='SubCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('course_image', models.ImageField(upload_to='images/')),
                ('course_desc', models.TextField(max_length=200)),
                ('course_fee', models.IntegerField(default=0)),
                ('main_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LearnwingApp.course')),
            ],
        ),
    ]
