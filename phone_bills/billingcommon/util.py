import math
import re


PHONE_NUMBER_RE = re.compile('^(?P<area_code>[0-9]{2})(?P<phone_number>[0-9]{8,9})$')


def extract_phone_number(str_phone):
    m = PHONE_NUMBER_RE.match(str_phone)
    if m:
        return m.group('area_code'), m.group('phone_number')
    raise ValueError('Not a phone number.')


def call_duration(start_ts, end_ts):
    td = end_ts - start_ts
    return math.floor(td.total_seconds()/60)