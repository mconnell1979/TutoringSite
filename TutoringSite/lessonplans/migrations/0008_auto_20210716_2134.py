# Generated by Django 3.2.4 on 2021-07-17 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplans', '0007_lessonplan_air_write_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplan',
            name='air_write_words',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='lessonplan',
            name='note',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
