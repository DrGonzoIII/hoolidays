from django.db import models
from django.conf import settings


# Create your models here.
class Holidays(models.Model):
    holiday_date = models.DateField()
    note = models.CharField(max_length=200)
    hours = models.IntegerField(default=8)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,)
