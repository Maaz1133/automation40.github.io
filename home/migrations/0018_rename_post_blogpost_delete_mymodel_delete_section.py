# Generated by Django 4.1.6 on 2023-02-23 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_section_paragraph'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='BlogPost',
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
