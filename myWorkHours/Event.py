__author__ = 'eMko'

from datetime import datetime

class EventTypes(object):
    """ The types of event
    """

    ARRIVAL = 1
    """ The constant for arrival event type """

    LEAVE = 2
    """ The constant for exit event type """

class Event(object):
    ''' data class for one log event
    '''

    datetime = datetime(1900, 1, 1)
    """ the date and time when this event occured """

    eventType = 0
    """ the type of event, should be from EventTypes constants """

    def __init__(self, datetime, eventType = 0):
        """ Inits the event.
            @param datetime the date and time when this event occurred; should be datetime.datetime type
            @param eventType the type constant from EventTypes
        """
        self.datetime = datetime
        self.eventType = eventType



