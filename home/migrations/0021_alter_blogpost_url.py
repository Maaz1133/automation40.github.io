# Generated by Django 4.1.6 on 2023-02-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_blogpost_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='URL',
            field=models.TextField(max_length=130),
        ),
    ]
