# Generated by Django 4.2.4 on 2023-08-26 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_alter_filenames_options_alter_filenames_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileNames',
        ),
        migrations.RemoveField(
            model_name='section',
            name='image',
        ),
    ]
