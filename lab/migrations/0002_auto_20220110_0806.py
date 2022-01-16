# Generated by Django 3.2.9 on 2022-01-10 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='difficulty',
            options={'verbose_name_plural': 'Difficulties'},
        ),
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lab.difficulty', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.category', verbose_name='Difficulty'),
        ),
    ]