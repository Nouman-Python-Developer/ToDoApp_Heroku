# Generated by Django 3.2.9 on 2021-11-09 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_alter_task_task_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 9, 10, 10, 9, 127550)),
        ),
    ]
