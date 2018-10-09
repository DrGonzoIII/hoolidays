from datetime import timedelta
import datetime


def daterange(year):

    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year + 1, 1, 1)
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


total = 0.0
for single_date in daterange(2018):
    if single_date.today().weekday() == 0:
        total += 8.5
    elif single_date.today().weekday() == 1:
        total += 8.5
    elif single_date.today().weekday() == 2:
        total += 8.5
    elif single_date.today().weekday() == 3:
        total += 8.5
    elif single_date.today().weekday() == 4:
        total += 6

    # print (single_date.strftime("%Y-%m-%d"))
print("Total Horas: " + str(total))
