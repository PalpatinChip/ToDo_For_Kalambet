# Generated by Django 5.0.3 on 2024-03-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_datetime_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_date',
            field=models.DateField(verbose_name=''),
        ),
    ]
