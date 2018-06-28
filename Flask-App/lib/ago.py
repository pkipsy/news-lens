from datetime import (
  datetime,
  timedelta,
)

units = ('year', 'day', 'hour', 'minute', 'second', 'millisecond', 'microsecond')

def get_delta_from_subject(subject):
    subject_type = type(subject)
    if subject_type is timedelta:
        delta = subject
    else:
        if subject_type is int or subject_type is float:
            dt = datetime.fromtimestamp(float(subject))
        else:
            # assume subject is a datetime object and strip timezone data.
            dt = subject.replace(tzinfo=None)
        # finally, create a timedelta from datetime.
        delta = datetime.now() - dt
    return delta

def delta2dict(delta):
    """Accepts a delta, returns a dictionary of units"""
    delta = abs(delta)
    return {
        'year'   : int(delta.days / 365),
        'day'    : int(delta.days % 365),
        'hour'   : int(delta.seconds / 3600),
        'minute' : int(delta.seconds / 60) % 60,
        'second' : delta.seconds % 60,
        'millisecond' : delta.microseconds/1000,
        'microsecond' : delta.microseconds%1000,
    }

def human(subject, precision=2, past_tense='{} ago', future_tense='in {}', abbreviate=False):
    """
    Accept a subject, return a human readable timedelta string.

    :param subject: a datetime, timedelta, or timestamp (integer / float) object
    :param precision: the desired amount of unit precision (default: 2)
    :param past_tense: the format string used for a past timedelta (default: '{} ago')
    :param future_tense: the format string used for a future timedelta (default: 'in {}')
    :param abbreviate: boolean to abbreviate units (default: False)

    :returns: Human readable timedelta string (Str)
    """
    delta = get_delta_from_subject(subject)
    the_tense = future_tense if delta < timedelta(0) else past_tense

    d = delta2dict( delta )

    hlist = []
    count = 0

    # start building up the output in the hlist.
    for unit in units:
        if count >= precision: break # met precision
        if d[ unit ] == 0: continue # skip 0's
        if abbreviate:
            if unit == 'millisecond':
                abr = 'ms'
            elif unit == 'microsecond':
                abr = 'um'
            else:
                abr = unit[0]
            hlist.append('{}{}'.format(d[unit], abr))
        else:
            s = '' if d[ unit ] == 1 else 's' # handle plurals
            hlist.append('{} {}{}'.format(d[unit], unit, s))
        count += 1

    return the_tense.format(', '.join(hlist))
