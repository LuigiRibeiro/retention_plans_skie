import datetime as dt

list_retention_plans = ['standard', 'gold', 'platinum ']


def last_day_month(year, month):
    date_control = dt.date(year, month, 1)
    next_month = date_control.replace(day=28) + dt.timedelta(days=4)
    return next_month - dt.timedelta(days=next_month.day)


def check_retention(date, retention_plan):
    """
    Determines whether an ERP snapshot should be kept or removed based on a specified retention plan.

    Args:
    - retention_plan (str): the retention plan to consider, which can be 'standard', 'gold', or 'platinum'.
    - date (datetime.date): the date of the snapshot to be checked.

    Returns:
    - bool: True if the snapshot should be retained, False if it should be deleted.

    Raises:
    - ValueError: if the provided plan is not recognized.
    - ValueError: if the date is not valid.
    """

    if retention_plan not in ['standard', 'gold', 'platinum']:
        raise 'Plan is not recognized'

    try:
        day_plan = date.day
        month_plan = date.month
        year_plan = date.year
    except:
        raise 'Date is not valid'

    today = dt.date.today()
    difference_dates = today - date
    difference_days = difference_dates.days
    difference_months = (today.year - date.year) * 12 + (today.month - date.month)
    difference_years = today.year - date.year

    if retention_plan == 'standard':
        return True if difference_days <= 42 else False
    elif retention_plan == 'gold':
        if last_day_month(year_plan, month_plan) == date:
            return True if difference_months <= 12 else False
        else:
            return True if difference_days <= 42 else False
    else:
        if dt.date(year_plan, 12, 31) == date:
            return True if difference_years <= 7 else False
        elif last_day_month(year_plan, month_plan) == date:
            return True if difference_months <= 12 else False
        else:
            return True if difference_days <= 42 else False