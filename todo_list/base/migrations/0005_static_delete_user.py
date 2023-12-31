# Generated by Django 4.2.3 on 2023-07-07 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_user_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Static',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tasks', models.IntegerField(default=0)),
                ('completed_tasks', models.IntegerField(default=0)),
                ('in_progress_tasks', models.IntegerField(default=0)),
                ('pending_tasks', models.IntegerField(default=0)),
                ('overdue_tasks', models.IntegerField(default=0)),
                ('high_priority_tasks', models.IntegerField(default=0)),
                ('average_completion_time', models.FloatField(default=0.0)),
                ('tasks_per_category', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
