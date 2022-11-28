""" Regular Expressions

Notes:

We are going to make some examples to use regular expressions

CheatSheet:
    ^ asserts position at start of the string

    \d matches a digit (equivalent to [0-9])

    (?P<foo>...) Name capture group foo for ... definition

    | alternatives

    $ asserts position at the end of the string
"""
# Requiered imports
import re


def get_TimeUnits(time_string):
    '''
    Given a time in HH:MM:SS(AM/PM) format,
    fetch every one of the items in a different Variable.
    '''
    # Generate Pattern
    pattern = r"^(?P<hour>\d{2}):(?P<minutes>\d{2}):(?P<seconds>\d{2})(?P<meridian>AM|PM)$"
    match = re.match(pattern, time_string)  # Run match
    # Extract data if possible
    if match:
        return (
            int(match.group("hour")),
            int(match.group("minutes")),
            int(match.group("seconds")),
            match.group("meridian")
        )


if __name__ == "__main__":
    timestring = "10:01:45AM"
    tup = get_TimeUnits(timestring)
    assert 10 == tup[0]  # Hours
    assert 1 == tup[1]  # Minutes
    assert 45 == tup[2]  # Seconds
    assert 'AM' == tup[3]
