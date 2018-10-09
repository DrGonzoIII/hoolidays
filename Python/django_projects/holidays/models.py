from django.db import models
from django.conf import settings
import datetime
from datetime import timedelta


# Create your models here.
class Holidays(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,)


class LaboralHolidays(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    optional = models.BooleanField(default=False)


class LaboralYear(models.Model):
    year = models.IntegerField()
    num_hours = models.DecimalField()
    holidays_days = models.OneToManyField(LaboralHolidays)

    # Calculamos horas totales - horas convenio = dias libres
    def calculate_hours(self):
        total = 0.0
        for single_date in self.daterange(self.year):
            if single_date.today().weekday() == 0:
                if single_date not in self.holidays_days.date:
                    total += 8.5
            elif single_date.today().weekday() == 1:
                if single_date not in self.holidays_days.date:
                    total += 8.5
            elif single_date.today().weekday() == 2:
                if single_date not in self.holidays_days.date:
                    total += 8.5
            elif single_date.today().weekday() == 3:
                if single_date not in self.holidays_days.date:
                    total += 8.5
            elif single_date.today().weekday() == 4:
                if single_date not in self.holidays_days.date:
                    total += 6
        return total

    def daterange(year):
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year + 1, 1, 1)
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
