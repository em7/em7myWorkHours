__author__ = 'eMko'

""" The command line interface for myWorkHours """

import sys
import fileinput
from myWorkHours import Counter,\
    Event,\
    InvalidEventTypeOrderException,\
    InvalidEventOverlapException,\
    InsufficientEventsException,\
    Parser

def print_help():
    """
     prints help after user uses the argument -h or --help
    """
    print("""myWorkHours_cli is a CLI for a program for counting the
time spent in work. Uses the format used by WebTerm software.
version 1.0.1
distributed under the terms and conditions of WTFPL www.wtfpl.net

usage: myWork [arg]
where: arg can be   -h or --help or /? for this help

If the LEAVE event is last, it is used as the end of the list. If the
ARRIVAL is last, it is counted that the last LEAVE event is now. So
it counts the time you have spent in work till now.""")

def parse_events():
    """
     Tries to parse the input, convert it to events

     @returns list of Event
    """

    events = []
    lines = sys.stdin.readlines()
    for line in lines:
        if not line.strip(): continue #skip empty lines
        try:
            event = Parser.parse_from_str(line)
            events.append(event)
        except Exception as exc:
            if len(exc.args) > 0: excMsg = exc.args[0]
            print("The event '" + line.strip("\n") + "' could not be parsed:\n" + excMsg, file=sys.stderr)
    return events

def count_events(events):
    """
     Counts the worktime based on events

     @param events the parsed events list
     @type events list of Event

     @return timedelta
    """
    assert isinstance(events, list)
    return Counter.count_event_list(events)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "/?":
            print_help()
            return

    try:
        events = parse_events()
        delta = count_events(events)
        print(delta)
    except Exception as e:
        print("An error occurred:", file=sys.stderr)
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()

