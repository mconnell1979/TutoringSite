# Generated by Django 3.2.5 on 2021-07-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonplans', '0036_alter_lessonplan_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonplan',
            name='scheduled',
            field=models.DateTimeField(blank=True, help_text='scheduled time for lesson to be given', null=True),
        ),
    ]
