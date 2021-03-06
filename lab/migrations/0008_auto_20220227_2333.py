# Generated by Django 3.2.9 on 2022-02-27 23:33

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0007_auto_20220227_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='objective',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
