import datetime


def get_current_time():
    moscow_tz = datetime.timezone(datetime.timedelta(hours=3))
    return datetime.datetime.now(tz=moscow_tz)


def today_date():
    return get_current_time().strftime('%Y-%m-%d')


def today_datetime():
    return get_current_time().strftime('%Y-%m-%d %H:%M:%S')
