# Generated by Django 4.0.2 on 2022-02-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=500)),
                ('projects', models.CharField(blank=True, max_length=120)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
