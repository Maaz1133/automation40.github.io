# Generated by Django 4.1.6 on 2023-02-23 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_post_blogpost_delete_mymodel_delete_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='content1',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]