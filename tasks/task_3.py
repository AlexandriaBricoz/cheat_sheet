from datetime import date


def datef(day: date):
    return day < date.today()


print(datef(date(2044, 3, 5)))
