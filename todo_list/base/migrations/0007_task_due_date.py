# Generated by Django 4.2.3 on 2023-07-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=None),
        ),
    ]
