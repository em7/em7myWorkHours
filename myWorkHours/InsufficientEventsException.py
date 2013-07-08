__author__ = 'eMko'

class InsufficientEventsException(Exception):
    """
     When the number of events to count is not at least two
    """
    pass