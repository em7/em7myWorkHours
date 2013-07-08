import unittest

from myWorkHours import Parser
from datetime import datetime
from myWorkHours.Event import EventTypes

__author__ = 'eMko'

class TestParser(unittest.TestCase):
    ''' the tests for Parser
    '''

    def test_parser_should_parse_testcase(self):
        eventLine = "8.7.2013 8:12:27   Příchod >   běžný průchod"
        eventType = EventTypes.ARRIVAL
        eventDate = datetime.strptime("8.7.2013 8:12:27", "%d.%m.%Y %H:%M:%S")
        parsedEvent = Parser.parse_from_str(eventLine)
        self.assertEqual(eventDate, parsedEvent.datetime, "The parsed datetime should be correct")
        self.assertEqual(eventType, parsedEvent.type, "The parsed event type should be correct")

    def test_parser_should_rise_exception_bad_format(self):
        eventLine = "8fsfdsfsd1.2.2113 8:12:fds27 fdsPřífsfsěžný průchodf"
        with self.assertRaises(Exception):
            parsedEvent = Parser.parse_from_str(eventLine)

    def test_parser_should_have_correct_type(self):
        eventArr = "8.7.2013 8:12:27   Příchod >   běžný průchod"
        eventEx = "8.7.2013 11:24:01     Odchod <   Lunch"
        parsedArr = Parser.parse_from_str(eventArr)
        parsedEx = Parser.parse_from_str(eventEx)
        self.assertEqual(parsedArr.type, EventTypes.ARRIVAL, "Arrival event should have a type of Arrival")
        self.assertEqual(parsedEx.type, EventTypes.EXIT, "Exit event should have a type of Exit")

    def test_parser_should_raise_exception_bad_datetime_format(self):
        eventLine = "81.2.2113 8:12:27   Příchod >   běžný průchod"
        with self.assertRaises(Exception):
            parsedEvent = Parser.parse_from_str(eventLine)

    def test_parser_should_raise_exception_bad_type_sign(self):
        eventLine = "8.7.2013 8:12:27   Příchod %   běžný průchod"
        with self.assertRaises(Exception):
            parsedEvent = Parser.parse_from_str(eventLine)