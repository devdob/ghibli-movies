# Generated by Django 2.1 on 2018-08-15 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20180815_2032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieCharacters',
            new_name='MovieCharacter',
        ),
    ]
