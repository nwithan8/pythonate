from datetime import datetime
from typing import Union


def remove_time_from_date(date_string: Union[datetime, str]) -> str:
    """
    Remove time, i.e. 00:00:00, from a datetime.datetime or string
    :param date_string: datetime.datetime object or string to convert
    :return: str without time, i.e. 2020-08-29
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return date_string.strftime("%Y-%m-%d")


def get_year_from_date(date_string: Union[datetime, str]) -> int:
    """
    Extract year from a datetime.datetime or string
    :param date_string: datetime.datetime object or string
    :return: int of year, i.e. 2020
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return int(date_string.strftime("%Y"))


def string_to_datetime(date_string: str, template: str = "%Y-%m-%dT%H:%M:%S") -> datetime:
    """
    Convert a string to a datetime.datetime object
    :param date_string: datetime string to convert
    :param template: (Optional) datetime template to use when parsing string (Default: "%Y-%m-%dT%H:%M:%S")
    :return: datetime.datetime object
    """
    if date_string.endswith('Z'):
        date_string = date_string[:-5]
    return datetime.strptime(date_string, template)


def datetime_to_string(datetime_object: datetime, template: str = "%Y-%m-%dT%H:%M:%S.000Z") -> str:
    """
    Convert a datetime.datetime object to a string
    :param datetime_object: datetime.datetime object to convert
    :param template: (Optional) datetime template to use when parsing string
    :return: str representation of datetime
    """
    return datetime_object.strftime(template)


def adjust_datetime_for_timezone(local_time: datetime) -> datetime:
    """
    Shift datetime.datetime in regards to UTC time
    :param local_time: local time datetime.datetime object
    :return: Shifted datetime.datetime object
    """
    difference = datetime.now() - datetime.utcnow()
    return local_time - difference


def hours_difference_in_timezone() -> int:
    """
    Get the hours difference between local and UTC time
    :return: int number of hours
    """
    return int((datetime.utcnow() - datetime.now()).total_seconds() / 60 / 60)


def get_nearest_30_minute_mark(time_format: str = "%Y-%m-%dT%H:%M:%S.000Z") -> str:
    """
    Get the most recently past hour or half-hour time
    :param time_format: (Optional) Format of timestamp (Default: "%Y-%m-%dT%H:%M:%S.000Z")
    :return: str of datetime
    """
    now = datetime.utcnow()
    if now.minute >= 30:
        now = now.replace(second=0, microsecond=0, minute=30)
    else:
        now = now.replace(second=0, microsecond=0, minute=0)
    return now.strftime(time_format)


def get_milliseconds_between_two_hours(start_hour: int, end_hour: int) -> int:
    """
    Get how many milliseconds between two 24-hour hours
    :param start_hour: starting hour (in 24-hour time)
    :param end_hour: ending hour (in 24-hour time)
    :return: int of milliseconds between the two hours
    """
    start_date = datetime(2020, 1, 1, start_hour, 0)
    if end_hour < start_hour:
        end_date = datetime(2020, 1, 2, end_hour, 0)
    else:
        end_date = datetime(2020, 1, 1, end_hour, 0)
    return int((end_date - start_date).total_seconds()) * 1000


def get_milliseconds_between_two_datetimes(start_datetime: datetime, end_datetime: datetime) -> int:
    """
    Get how many milliseconds between two datetime.datetime objects
    :param start_datetime: starting datetime.datetime object
    :param end_datetime: ending datetime.datetime object
    :return: int of milliseconds between the two datetime.datetime objects
    """
    return int((end_datetime - start_datetime).total_seconds()) * 1000
