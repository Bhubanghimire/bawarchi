# Generated by Django 4.1.7 on 2023-03-08 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0018_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
