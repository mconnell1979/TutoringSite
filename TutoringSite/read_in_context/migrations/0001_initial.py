# Generated by Django 3.2.5 on 2021-08-26 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SRABook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Getting the Main Idea', max_length=100)),
                ('orig_book', models.CharField(help_text='A', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SRAPassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_num', models.IntegerField(help_text='Unit #')),
                ('passage', models.TextField(help_text='Passage or Paragraph - Max 1000 characters', max_length=1000)),
                ('question', models.CharField(help_text='What is the main idea?', max_length=255)),
                ('choiceA', models.CharField(max_length=255)),
                ('choiceB', models.CharField(max_length=255)),
                ('choiceC', models.CharField(max_length=255)),
                ('choiceD', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='read_in_context.srabook')),
            ],
        ),
    ]
