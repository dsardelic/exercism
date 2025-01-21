import calendar
import datetime


class MeetupDayException(ValueError):
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    first_day_in_month, days_in_month = calendar.monthrange(year, month)
    dates = tuple(
        i + 1
        for i in range(days_in_month)
        if (first_day_in_month + i) % 7 == getattr(calendar, day_of_week.upper())
    )
    if week == "first":
        date = dates[0]
    if week == "second":
        date = dates[1]
    if week == "third":
        date = dates[2]
    if week == "fourth":
        date = dates[3]
    if week == "fifth":
        try:
            date = dates[4]
        except IndexError as err:
            raise MeetupDayException("That day does not exist.") from err
    if week == "last":
        date = dates[-1]
    if week == "teenth":
        date = next(date for date in dates if date in range(13, 20))
    return datetime.date(year, month, date)
