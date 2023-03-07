# Generated by Django 4.1.7 on 2023-02-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_about_alter_contactus_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='email',
            new_name='primary_email',
        ),
        migrations.AddField(
            model_name='about',
            name='secondary_email',
            field=models.EmailField(default='abc@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]