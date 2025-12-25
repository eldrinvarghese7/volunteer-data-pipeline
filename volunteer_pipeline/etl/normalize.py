from dateutil import parser
import logging

def clean_name(name):
    if not isinstance(name, str):
        return None
    return " ".join(name.strip().title().split())

def clean_date(date_str):
    try:
        return parser.parse(date_str, dayfirst=True).date().isoformat()
    except:
        return None
