#!/usr/bin/env python3
"""
This project module contains a logging module
"""
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError


def filter_datum(fields, redaction, message, separator):
    """
    This is a function that uses a regex to replace
    occurrences of certain field values.
    Returns:
        The log message obfuscated.
    """
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))
