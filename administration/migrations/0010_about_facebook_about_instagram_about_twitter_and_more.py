# Generated by Django 4.1.7 on 2023-03-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0009_openinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.CharField(default='#', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='instagram',
            field=models.CharField(default='#', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='about',
            name='youtube',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]