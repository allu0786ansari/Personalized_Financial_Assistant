# Generated by Django 5.1.1 on 2024-11-09 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
    ]
