import datetime


def add(moment):
    return moment + datetime.timedelta(seconds=1_000_000_000)
