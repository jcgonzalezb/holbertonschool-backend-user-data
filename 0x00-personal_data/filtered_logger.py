#!/usr/bin/env python3
"""
This project module contains a logging module
"""
import re


def filter_datum(fields, redaction, message, separator):
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))
