# Generated by Django 4.2.3 on 2023-07-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name='date created')),
                ('status', models.BooleanField()),
                ('importance', models.CharField(choices=[('pending', 'В очікуванні'), ('in_progress', 'В процесі'), ('completed', 'Завершено')], default='pending', max_length=30)),
                ('category', models.CharField(choices=[('myself', 'Саморозвиток'), ('rest', 'Відпочинок'), ('comertion', 'Комерація'), ('organization', 'Організація'), ('development', 'Розробка'), ('maintence', 'Хазяйство'), ('none', 'Невизначена')], default='none', max_length=30)),
                ('subjects', models.CharField(max_length=30)),
                ('objects_of_plening', models.CharField(max_length=30)),
            ],
        ),
    ]
