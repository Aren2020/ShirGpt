# Generated by Django 4.2.4 on 2023-09-18 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0013_delete_filenames_remove_section_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api', models.CharField(max_length=50)),
                ('starttime', models.CharField(default='NONTOUCH', max_length=50)),
                ('trycount', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('disable', models.BooleanField(default=False)),
            ],
        ),
    ]
