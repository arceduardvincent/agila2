# Generated by Django 3.2.9 on 2022-02-27 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0009_auto_20220227_2334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='content',
        ),
    ]
