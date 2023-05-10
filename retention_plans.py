import datetime as dt

list_retention_plans = ['Standard', 'Gold', 'Platinum ']


def last_day_month(year, month):
    date_control = dt.datetime(year, month, 1)
    next_month = date_control.replace(day=28) + dt.timedelta(days=4)
    return next_month - dt.timedelta(days=next_month.day)


def check_retention():
    pass