# Generated by Django 4.0.2 on 2022-02-17 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotlight', '0002_projects'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]
