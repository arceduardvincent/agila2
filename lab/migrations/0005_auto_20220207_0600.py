# Generated by Django 3.2.9 on 2022-02-07 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0004_auto_20220124_0613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscribercoursestatus',
            options={'ordering': ['-created'], 'verbose_name': 'SubscriberCourseStatus', 'verbose_name_plural': 'SubscriberCourseStatuses'},
        ),
        migrations.AddField(
            model_name='course',
            name='short_description',
            field=models.CharField(default=1, max_length=250, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=250, null=True, verbose_name='Title'),
        ),
    ]
