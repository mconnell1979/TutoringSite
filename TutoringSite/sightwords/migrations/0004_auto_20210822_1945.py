# Generated by Django 3.2.5 on 2021-08-23 00:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sightwords', '0003_sightwordsentences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sightwordsentences',
            name='sight_word1',
        ),
        migrations.AddField(
            model_name='sightwordsentences',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sightwordsentences',
            name='sight_word',
            field=models.ManyToManyField(blank=True, to='sightwords.SightWord'),
        ),
        migrations.AddField(
            model_name='sightwordsentences',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]