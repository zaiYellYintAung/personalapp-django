# Generated by Django 4.2 on 2023-05-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='tags',
        ),
        migrations.AddField(
            model_name='projects',
            name='tags',
            field=models.ManyToManyField(to='projectlist.tags'),
        ),
    ]
