# Generated by Django 4.2 on 2023-05-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogs_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
            ],
        ),
        migrations.AddField(
            model_name='blogs',
            name='topic',
            field=models.ManyToManyField(to='blogs.topic'),
        ),
    ]