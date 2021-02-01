from django.db import models

# Create your models here.

class BuyRecord(models.Model):
    company = models.CharField(max_length=50)
    share = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    log = models.IntegerField(null=True, blank=True)


class AAPL(models.Model):
    date = models.DateTimeField()
    high = models.IntegerField()
    low = models.IntegerField()
    open = models.IntegerField()
    close = models.IntegerField()

class Meta:
    ordering = ("-date")

def __str__(self):
    pass


