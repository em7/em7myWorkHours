from myWorkHours.InsufficientEventsException import InsufficientEventsException

__author__ = 'eMko'

import unittest
from datetime import datetime, timedelta
from myWorkHours import Counter
from myWorkHours.Event import *
from myWorkHours.InvalidEventTypeOrderException import InvalidEventTypeOrderException
from myWorkHours.InvalidEventOverlapException import InvalidEventOverlapException

class TestCounter(unittest.TestCase):

    def test_difference_if_arrival_before_exit_then_timedelta(self):
        event1 = Event(datetime(2012,1,5,12,30,25), EventTypes.ARRIVAL)
        event2 = Event(datetime(2012,1,5,14,15,40), EventTypes.EXIT)
        delta = Counter.difference(event1, event2)
        self.assertEqual(delta, timedelta(0, 15, 0, 0, 45, 1),
                         "The timedelta should be positive and correct for arrival before exit events" )

    def test_difference_if_exit_before_arrival_then_0(self):
        event1 = Event(datetime(2012,1,5,12,30,25), EventTypes.EXIT)
        event2 = Event(datetime(2012,1,5,14,15,40), EventTypes.ARRIVAL)
        delta = Counter.difference(event1, event2)
        self.assertEqual(delta, timedelta(0),
                         "The timedelta should be 0 for exit before arrival")

    def test_difference_if_not_good_event_type_order_raise_exception(self):
        evt1 = Event(datetime(2012,1,5,12,30,25), EventTypes.EXIT)
        evt2 = Event(datetime(2012,1,5,14,15,40), EventTypes.EXIT)
        evt3 = Event(datetime(2012,1,5,12,30,25), EventTypes.ARRIVAL)
        evt4 = Event(datetime(2012,1,5,14,15,40), EventTypes.ARRIVAL)

        with self.assertRaises(InvalidEventTypeOrderException):
            Counter.difference(evt1, evt2)
        with self.assertRaises(InvalidEventTypeOrderException):
            Counter.difference(evt3, evt4)

    def test_difference_events_overlap_raise_exception(self):
        evt1 = Event(datetime(2012,1,5,14,15,40), EventTypes.EXIT)
        evt2 = Event(datetime(2012,1,5,12,30,25), EventTypes.ARRIVAL)

        with self.assertRaises(InvalidEventOverlapException):
            Counter.difference(evt1, evt2)


    def test_count_events_list_ends_with_exit(self):
        events = [Event(datetime(2012,1,5,7,15,25), EventTypes.ARRIVAL),
                  Event(datetime(2012,1,5,11,30,0), EventTypes.EXIT),
                  Event(datetime(2012,1,5,12,5,30), EventTypes.ARRIVAL),
                  Event(datetime(2012,1,5,15,50,55), EventTypes.EXIT)]
        delta = Counter.count_event_list(events)
        self.assertEqual(delta, timedelta(0, 0, 0, 0, 0, 8), "The difference between ARRIVAL and EXIT should be correct")

    def test_count_events_list_not_end_with_exit_use_now(self):
        events = [Event(datetime(2012,1,5,7,15,25), EventTypes.ARRIVAL),
                  Event(datetime(2012,1,5,11,30,0), EventTypes.EXIT),
                  Event(datetime(2012,1,5,12,5,30), EventTypes.ARRIVAL)]
        now = datetime.now()
        delta = Counter.count_event_list(events)
        expectedDelta = timedelta(0, 15275) + (datetime.now() - datetime(2012,1,5,12,5,30))
        self.assertAlmostEqual(expectedDelta, delta, None,
                               "If the EXIT event is not last, the now datetime should be used as approximation",
                               timedelta(0, 2))

    def test_count_events_list_at_last_two(self):
        with self.assertRaises(InsufficientEventsException):
            Counter.count_event_list([Event(datetime(2012,1,5,7,15,25), EventTypes.ARRIVAL)])

    def test_count_events_list_arrival_first(self):
        with self.assertRaises(InvalidEventTypeOrderException):
            Counter.count_event_list([Event(datetime(2012,1,5,11,30,0), EventTypes.EXIT),
                                      Event(datetime(2012,1,5,7,15,25), EventTypes.ARRIVAL)])

    def test_count_events_list_events_should_be_list(self):
        with self.assertRaises(Exception):
            Counter.count_event_list(None)

        with self.assertRaises(Exception):
            Counter.count_event_list(Event(datetime(2012,1,5,11,30,0), EventTypes.EXIT))