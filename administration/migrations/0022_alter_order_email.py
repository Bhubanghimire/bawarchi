# Generated by Django 4.1.7 on 2023-03-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0021_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
