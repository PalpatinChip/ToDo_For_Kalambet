# Generated by Django 5.0.3 on 2024-03-18 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
