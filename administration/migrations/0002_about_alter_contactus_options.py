# Generated by Django 4.1.7 on 2023-02-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.ImageField(upload_to='logo')),
                ('sub_title', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('primary_contact', models.CharField(max_length=20)),
                ('secondary_contact', models.CharField(max_length=20)),
                ('openning_hours', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'CONTACT US'},
        ),
    ]
