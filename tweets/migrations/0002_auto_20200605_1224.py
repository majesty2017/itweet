# Generated by Django 2.2 on 2020-06-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tweets',
            new_name='Tweet',
        ),
    ]
