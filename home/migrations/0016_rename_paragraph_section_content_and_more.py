# Generated by Django 4.1.6 on 2023-02-23 16:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_section'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='paragraph',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='section',
            name='heading',
        ),
        migrations.AddField(
            model_name='section',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='home.post'),
        ),
    ]