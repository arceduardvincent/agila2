# Generated by Django 3.2.9 on 2022-01-24 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
