

__author__ = 'eMko'
""" Module for counting the time between events """

from datetime import datetime,timedelta
from collections import Iterable
from myWorkHours.Event import EventTypes, Event
from myWorkHours.InvalidEventTypeOrderException import InvalidEventTypeOrderException
from myWorkHours.InvalidEventOverlapException import InvalidEventOverlapException
from myWorkHours.InsufficientEventsException import InsufficientEventsException

def difference(event1, event2):
    """
     Counts the time difference between event1 and event2. The time difference
     is equal to timedelta between the times when the events occur if the
     event of type ARRIVAL is before EXIT. If EXIT is before ARRIVAL, then the
     result is 0

     If both of the events have the same type, the InvalidEventTypeOrderException
     is raised.

     If the events overlaps, i.e. event2 is before the event1, the InvalidEventOverlapException
     is raised.

     @param event1 Event the first event
     @param event2 Event the second event
    """

    if event1.eventType == event2.eventType:
        raise InvalidEventTypeOrderException("The both events have the same type, which is not valid. Should be altering EXIT and ARRIVAL.")

    if event2.datetime < event1.datetime:
        raise InvalidEventOverlapException("The event2 is before the event1.")

    if event1.eventType == EventTypes.EXIT and event2.eventType == EventTypes.ARRIVAL:
        return timedelta(0)

    delta = event2.datetime - event1.datetime

    return delta

def count_event_list(events):
    """
     Counts the time between events of ARRIVAL type and the EXIT type, leaving the gaps between EXIT and ARRIVAL.

     If the events are not Iterable, the Exception is raised.

     If there are less than 2 events, the InsufficientEventsException is raised

     If the two following events have the same type or the ARRIVAL is not as first, the InvalidEventTypeOrderException
     is raised.

     If the two following events overlaps, i.e. event2 is before the event1, the InvalidEventOverlapException
     is raised.

     @param events the list of Events to count
     @returns datetime.timedelta with difference between the events
    """

    if not (isinstance(events, Iterable)):
        raise Exception("The events should be a iterable with events")

    if len(events) < 2:
        raise InsufficientEventsException("There should be at least 2 events in the list")

    if events[0].eventType != EventTypes.ARRIVAL:
        raise InvalidEventTypeOrderException("The ARRIVAL event should be first.")

    #is this the pythonic way how to do a foldl?
    acc = timedelta(0)
    previous_event = events[0]
    for event in events[1:]:
        delta = difference(previous_event, event)
        acc = acc + delta
        previous_event = event

    #if the EXIT event is not as last, do the approximation
    if events[-1].eventType != EventTypes.EXIT:
        lastFakeEvt = Event(datetime.now(), EventTypes.EXIT)
        delta = difference(previous_event, lastFakeEvt)
        acc = acc + delta

    return acc