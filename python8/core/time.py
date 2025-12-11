import time
from datetime import datetime, timedelta, date
from typing import Union


def unix_timestamp_now():
    """
    Get the current Unix timestamp.
    """
    return int(time.time())


def datetime_now() -> datetime:
    """
    Get the current datetime.
    """
    return datetime.now()


def datetime_today() -> date:
    """
    Get the current date.
    """
    return datetime.today().date()


def unix_timestamp_seconds_ago(seconds: int):
    """
    Get the Unix timestamp for a specified number of seconds ago.

    :param seconds: The number of seconds to go back in time.
    :return: Unix timestamp for the specified number of seconds ago.
    """
    return int(time.time()) - seconds


def unix_timestamp_seconds_from_now(seconds: int):
    """
    Get the Unix timestamp for a specified number of seconds from now.

    :param seconds: The number of seconds to go forward in time.
    :return: Unix timestamp for the specified number of seconds from now.
    """
    return int(time.time()) + seconds


def datetime_seconds_ago(seconds: int):
    """
    Get the datetime for a specified number of seconds ago.

    :param seconds: The number of seconds to go back in time.
    :return: Datetime for the specified number of seconds ago.
    """
    return datetime.now() - timedelta(seconds=seconds)


def datetime_seconds_from_now(seconds: int):
    """
    Get the datetime for a specified number of seconds from now.

    :param seconds: The number of seconds to go forward in time.
    :return: Datetime for the specified number of seconds from now.
    """
    return datetime.now() + timedelta(seconds=seconds)


def unix_timestamp_minutes_ago(minutes: int):
    """
    Get the Unix timestamp for a specified number of minutes ago.

    :param minutes: The number of minutes to go back in time.
    :return: Unix timestamp for the specified number of minutes ago.
    """
    return int(time.time()) - minutes * 60


def unix_timestamp_minutes_from_now(minutes: int):
    """
    Get the Unix timestamp for a specified number of minutes from now.

    :param minutes: The number of minutes to go forward in time.
    :return: Unix timestamp for the specified number of minutes from now.
    """
    return int(time.time()) + minutes * 60


def datetime_minutes_ago(minutes: int):
    """
    Get the datetime for a specified number of minutes ago.

    :param minutes: The number of minutes to go back in time.
    :return: Datetime for the specified number of minutes ago.
    """
    return datetime.now() - timedelta(minutes=minutes)


def datetime_minutes_from_now(minutes: int):
    """
    Get the datetime for a specified number of minutes from now.

    :param minutes: The number of minutes to go forward in time.
    :return: Datetime for the specified number of minutes from now.
    """
    return datetime.now() + timedelta(minutes=minutes)


def unix_timestamp_hours_ago(hours: int):
    """
    Get the Unix timestamp for a specified number of hours ago.

    :param hours: The number of hours to go back in time.
    :return: Unix timestamp for the specified number of hours ago.
    """
    return int(time.time()) - hours * 60 * 60


def unix_timestamp_hours_from_now(hours: int):
    """
    Get the Unix timestamp for a specified number of hours from now.

    :param hours: The number of hours to go forward in time.
    :return: Unix timestamp for the specified number of hours from now.
    """
    return int(time.time()) + hours * 60 * 60


def datetime_hours_ago(hours: int):
    """
    Get the datetime for a specified number of hours ago.

    :param hours: The number of hours to go back in time.
    :return: Datetime for the specified number of hours ago.
    """
    return datetime.now() - timedelta(hours=hours)


def datetime_hours_from_now(hours: int):
    """
    Get the datetime for a specified number of hours from now.

    :param hours: The number of hours to go forward in time.
    :return: Datetime for the specified number of hours from now.
    """
    return datetime.now() + timedelta(hours=hours)


def unix_timestamp_days_ago(days: int):
    """
    Get the Unix timestamp for a specified number of days ago.

    :param days: The number of days to go back in time.
    :return: Unix timestamp for the specified number of days ago.
    """
    return int(time.mktime((datetime.today() - timedelta(days=days)).timetuple()))


def unix_timestamp_days_from_now(days: int):
    """
    Get the Unix timestamp for a specified number of days from now.

    :param days: The number of days to go forward in time.
    :return: Unix timestamp for the specified number of days from now.
    """
    return int(time.mktime((datetime.today() + timedelta(days=days)).timetuple()))


def datetime_days_ago(days: int):
    """
    Get the datetime for a specified number of days ago.

    :param days: The number of days to go back in time.
    :return: Datetime for the specified number of days ago.
    """
    return datetime.today() - timedelta(days=days)


def datetime_days_from_now(days: int):
    """
    Get the datetime for a specified number of days from now.

    :param days: The number of days to go forward in time.
    :return: Datetime for the specified number of days from now.
    """
    return datetime.today() + timedelta(days=days)


def datetime_to_string(dt: datetime, _format: str = "%Y-%m-%dT%H:%M:%S.000Z"):
    """
    Convert a datetime object to a string in ISO format.

    :param dt: datetime.datetime object to convert
    :type dt: datetime.datetime
    :param _format: (Optional) datetime template to use when parsing string
    :type _format: str
    :return: str representation of datetime
    :rtype: str
    """
    return dt.strftime(_format)


def unix_timestamp_to_datetime(timestamp: int):
    """
    Convert a Unix timestamp to a datetime object.
    """
    return datetime.fromtimestamp(timestamp)


def string_to_datetime(date_string: str, _format: str = "%Y-%m-%dT%H:%M:%S") -> datetime:
    """
    Convert a string to a datetime object

    :param date_string: datetime string to convert
    :type date_string: str
    :param _format: (Optional) datetime template to use when parsing string (Default: "%Y-%m-%dT%H:%M:%S")
    :type _format: str
    :return: datetime.datetime object
    :rtype: datetime.datetime
    """
    if date_string.endswith('Z'):
        date_string = date_string[:-5]
    return datetime.strptime(date_string, _format)


def string_to_unix_timestamp(date_string: str, _format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Convert a string to a Unix timestamp.
    """
    dt = string_to_datetime(date_string, _format)
    return int(dt.timestamp())


def unix_timestamp_to_string(timestamp: int, _format: str = "%Y-%m-%d %H:%M:%S"):
    """
    Convert a Unix timestamp to a string in ISO format.
    """
    dt = unix_timestamp_to_datetime(timestamp)
    return datetime_to_string(dt, _format)


def years_between(start_date: date, end_date: date) -> int:
    """
    Calculate the number of years between two dates.
    """
    return end_date.year - start_date.year - ((end_date.month, end_date.day) < (start_date.month, start_date.day))


def remove_time_from_date(date_string: Union[datetime, str]) -> str:
    """
    Remove time, i.e. 00:00:00, from a datetime.datetime or string

    :param date_string: datetime.datetime object or string to convert
    :type date_string: datetime.datetime or str
    :return: str without time, i.e. 2020-08-29
    :return: str
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return date_string.strftime("%Y-%m-%d")


def get_year_from_date(date_string: Union[datetime, str]) -> int:
    """
    Extract year from a datetime.datetime or string

    :param date_string: datetime.datetime object or string
    :type date_string: datetime.datetime or str
    :return: int of year, i.e. 2020
    :return: int
    """
    if type(date_string) == str:
        date_string = string_to_datetime(date_string=date_string)
    return int(date_string.strftime("%Y"))


def adjust_datetime_for_timezone(local_time: datetime) -> datetime:
    """
    Shift datetime.datetime in regards to UTC time

    :param local_time: local time datetime.datetime object
    :type local_time: datetime.datetime
    :return: Shifted datetime.datetime object
    :rtype: datetime.datetime
    """
    difference = datetime.now() - datetime.utcnow()
    return local_time - difference


def hours_difference_in_timezone() -> int:
    """
    Get the hours difference between local and UTC time

    :return: int number of hours
    :rtype: int
    """
    return int((datetime.utcnow() - datetime.now()).total_seconds() / 60 / 60)


def get_nearest_30_minute_mark(time_format: str = "%Y-%m-%dT%H:%M:%S.000Z") -> str:
    """
    Get the most recently past hour or half-hour time

    :param time_format: (Optional) Format of timestamp (Default: "%Y-%m-%dT%H:%M:%S.000Z")
    :type time_format: str
    :return: str of datetime
    :rtype: str
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
    :type start_hour: int
    :param end_hour: ending hour (in 24-hour time)
    :type start_hour: int
    :return: int of milliseconds between the two hours
    :rtype: int
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
    :type start_datetime: datetime.datetime
    :param end_datetime: ending datetime.datetime object
    :type end_datetime: datetime.datetime
    :return: int of milliseconds between the two datetime.datetime objects
    :rtype: int
    """
    return int((end_datetime - start_datetime).total_seconds()) * 1000
