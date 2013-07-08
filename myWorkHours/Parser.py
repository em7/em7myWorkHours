import re
from datetime import datetime
from myWorkHours.Event import *

""" A parser module for the events """

__author__ = 'eMko'


def parse_from_str(eventLine):
    """ parses the eventLine to a Event object
    The line should be of format like

    8.7.2013 8:12:27   Příchod >   běžný průchod

    where first part is datetime, next is some word followed by > for arrival and < for exit,
     last is comment which is ignored
    if eventLine is not a valid event, raises an Exception
    """

    parsed = re.match("(\\d{1,2}\.\\d{1,2}\.\\d{4} \\d{1,2}\:\\d{2}:\\d{2})[^<>]*([<>]{1}).*",
                      eventLine)
    if parsed is None:
        raise Exception("Could not parse an eventLine. Probably you have a wrong format")

    groups = parsed.groups()

    if len(groups) != 2:
        raise Exception("Could not parse an eventLine. Probably you have a wrong format")

    try:
        eventDate = datetime.strptime(groups[0], "%d.%m.%Y %H:%M:%S")
    except ValueError as ve:
        raise Exception("Could not parse an eventLine. The event date was in incorrect format. " +  ve.args[0])

    eventType = 0
    if groups[1] == ">": eventType = EventTypes.ARRIVAL
    if groups[1] == "<": eventType = EventTypes.EXIT

    if eventType == 0:
        raise Exception("Could not parse an eventLine. The sign which determines the type was not correct: " + groups[1])

    eventObj = Event(eventDate, eventType)
    return eventObj
