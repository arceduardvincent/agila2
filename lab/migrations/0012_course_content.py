# Generated by Django 3.2.9 on 2022-02-28 00:20

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_auto_20220227_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='content',
            field=tinymce.models.HTMLField(null=True, verbose_name='Content'),
        ),
    ]