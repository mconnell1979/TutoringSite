# Generated by Django 4.0.4 on 2022-06-21 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vv_stories', '0003_remove_vvstoryquestion_story_delete_vvstory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VVStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Imagine That! Stories', max_length=100)),
                ('number', models.IntegerField(help_text='Story #')),
                ('story', models.TextField(help_text='Write story here.')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vv_stories.vvstorybook')),
            ],
        ),
        migrations.CreateModel(
            name='VVStoryQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(help_text='What is the main idea of the story?', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vv_stories.vvstory')),
            ],
        ),
    ]
