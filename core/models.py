from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Event')
    description = models.TextField(blank = True, null = True)
    event_date = models.DateTimeField(verbose_name='Date of the Event')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Date of the event was register')
    user = models.ForeignKey (User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.title

