# Generated by Django 3.2.4 on 2021-07-17 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_student_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='created_at',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='updated_at',
            new_name='updated',
        ),
    ]
