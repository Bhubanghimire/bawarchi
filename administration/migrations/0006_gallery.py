# Generated by Django 4.1.7 on 2023-02-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0005_alter_about_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'GALLERY',
            },
        ),
    ]
