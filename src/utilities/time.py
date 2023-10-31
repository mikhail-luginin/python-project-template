import datetime


def get_current_time() -> datetime.datetime:
    moscow_tz = datetime.timezone(datetime.timedelta(hours=3))
    return datetime.datetime.now(tz=moscow_tz)


def today_date() -> str:
    return get_current_time().strftime("%Y-%m-%d")


def today_datetime() -> str:
    return get_current_time().strftime("%Y-%m-%d %H:%M:%S")
