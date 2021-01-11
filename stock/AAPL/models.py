from django.db import models

# Create your models here.

class AAPL(models.Model):
    date = models.DateTimeField()
    high = models.DateTimeField()
    low = models.IntegerField()
    open = models.IntegerField()
    close = models.IntegerField()

class Meta:
    ordering = ("-date")

def __str__(self):
    pass