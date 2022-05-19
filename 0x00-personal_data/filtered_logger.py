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
        """Initialize the class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Method to filter values in incoming log records using filter_datum.
            Returns: A log.
        """
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields, redaction, message, separator):
    """
    This is a function that uses a regex to replace
    occurrences of certain field values.
    Returns:
        The log message obfuscated.
    """
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))
