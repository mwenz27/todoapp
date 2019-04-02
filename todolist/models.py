from django.db import models
from django.db.models import CharField
# from django.utils import timezone
from datetime import datetime
# from django.utils.timezone import localtime, now
from django.utils.timezone import utc
import pytz



# Create your models here.



class TodoList(models.Model):
    title = models.CharField(max_length=200)
    completed = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:50]


class TodoItem(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name[:50]

    def days_left(self):
        today = datetime.utcnow().replace(tzinfo=utc)
        today = today.date()
        delta = (self.due_date - today)
        return f'{delta.days}'



