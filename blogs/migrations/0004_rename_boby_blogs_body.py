# Generated by Django 4.2 on 2023-05-13 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_topic_blogs_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='boby',
            new_name='body',
        ),
    ]
