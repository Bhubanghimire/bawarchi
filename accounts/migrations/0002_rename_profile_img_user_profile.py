# Generated by Django 4.1.7 on 2023-02-18 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='profile_img',
            new_name='profile',
        ),
    ]
