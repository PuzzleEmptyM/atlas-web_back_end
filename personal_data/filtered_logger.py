#!/usr/bin/env python3
"""
This function "filter_datum" returns a log message obfuscated
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Args: fields (list): fields to obfuscate
          redaction (str): string to replace the field value
          message (str): log message to be processed
          separator (str): separator used in the log message
    Return: (str): obfuscated log message
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  lambda m: m.group().split('=')[0] + '=' + redaction,
                  message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class to filter sensitive information in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with specified fields to redact.

        Args:
            fields (List[str]): fields to obfuscate
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.

        Args:
            record (logging.LogRecord): the log record to be formatted

        Returns:
            str: formatted log record with sensitive information redacted
        """
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original_message, self.SEPARATOR)
