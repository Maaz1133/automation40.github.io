# Generated by Django 4.1.6 on 2023-02-15 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_desc_home1_message1'),
    ]

    operations = [
        migrations.CreateModel(
            name='login1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_login', models.CharField(max_length=122)),
                ('email_login', models.CharField(max_length=122)),
                ('message2', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]