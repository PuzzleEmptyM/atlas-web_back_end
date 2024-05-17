#!/usr/bin/env python3
"""
This function "filter_datum" returns a log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    """
    Args: none
    Return: 
    """
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*',
                  lambda m: m.group().split('=')[0] + '=' + redaction,
                  message)
