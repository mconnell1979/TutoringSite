# Generated by Django 4.0.4 on 2022-06-25 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VVPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title Of The Image', max_length=100)),
                ('directions', models.TextField(help_text='Look at the picture before the lesson. Present the picture to the student. Say, Here is the pic...')),
                ('image', models.ImageField(upload_to='images/vv_pictures/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VVPictureBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Sentence by Sentence', max_length=100)),
                ('book', models.CharField(help_text='A', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VVPictureQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Question to the whole.', max_length=100)),
                ('number', models.IntegerField(help_text='Question Order #')),
                ('question', models.TextField(help_text="a. Start at top. \r For example: What should I picture for the dog's faceb. Use choice and contrast. \r For Example:Should I picture the dog with...")),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vv_pictures.vvpicture')),
            ],
        ),
        migrations.AddField(
            model_name='vvpicture',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vv_pictures.vvpicturebook'),
        ),
    ]
