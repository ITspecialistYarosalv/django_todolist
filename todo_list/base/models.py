from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User
class Task(models.Model):
    STATUS_CHOICE = [
        ('pending', 'В очікуванні'),
        ('in_progress', 'В процесі'),
        ('completed', 'Завершено'),
    ]
    IMPORTANCE = [
        ('normal','нормально'),
        ('not important',"не важливо"),
        ('very important',"дуже важливо")
    ]
    CATEGORY = [
        ('myself','Саморозвиток'),
        ("rest","Відпочинок"),
        ("comertion","Комерація"),
        ('organization','Організація'),
        ("development","Розробка"),
        ("maintence", "Хазяйство"),
        ("none", "Невизначена"),
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_at = models.DateTimeField("date created")
    status =  models.CharField(max_length=30,choices=STATUS_CHOICE,default='pending')
    importance = models.CharField(max_length=30,choices=IMPORTANCE,default='not important')
    category = models.CharField(max_length=30,choices=CATEGORY,default='none')
    subjects = models.CharField(max_length=30)
    objects_of_plening = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Static(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    total_tasks = models.IntegerField(default=0)  # Загальна кількість задач
    completed_tasks = models.IntegerField(default=0)  # Кількість виконаних задач
    in_progress_tasks = models.IntegerField(default=0)  # Кількість задач у процесі виконання
    pending_tasks = models.IntegerField(default=0)  # Кількість задач в очікуванні
    high_priority_tasks = models.IntegerField(default=0)  # Кількість задач з високим пріоритетом

    #Додайте інші числові поля, які вам потрібні для аналітики
    average_completion_time = models.FloatField(default=0.0)  # Середній час виконання задач
    tasks_per_category = models.IntegerField(default=0)  # Кількість задач за категоріями

    def calculate_statistics(self):
        # Обрахунок статистики тут
        self.total_tasks = Task.objects.count()
        self.completed_tasks = Task.objects.filter(status='completed').count()
        self.in_progress_tasks = Task.objects.filter(status='in_progress').count()
        self.pending_tasks = Task.objects.filter(status='pending').count()
        self.high_priority_tasks = Task.objects.filter(importance='very important').count()

        # Додаткові обрахунки статистики

        # Збереження змін у моделі
        self.save()

    def __str__(self):
        return self.user.username