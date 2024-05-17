#!/usr/bin/env python3
"""
This function "filter_datum" returns a log message obfuscated
"""
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
