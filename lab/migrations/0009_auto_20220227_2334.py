# Generated by Django 3.2.9 on 2022-02-27 23:34

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0008_auto_20220227_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='objective',
            field=tinymce.models.HTMLField(null=True, verbose_name='Objective'),
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=tinymce.models.HTMLField(null=True, verbose_name='Overview'),
        ),
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=tinymce.models.HTMLField(null=True, verbose_name='Prerequisites'),
        ),
    ]
