#!/usr/bin/env python3
"""
This function "filter_datum" returns a log message obfuscated
"""
import logging
import re
from typing import List
import os
import mysql.connector
from mysql.connector import connection


PII_FIELDS = ('email', 'phone', 'ssn', 'name', 'password')


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


def get_logger() -> logging.Logger:
    """
    Return: logging.Logger - logger configured to redact specific PII fields
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """
    Environment Variables:
        PERSONAL_DATA_DB_USERNAME (str): Database username, default 'root'.
        PERSONAL_DATA_DB_PASSWORD (str): Database password,\
            default an empty string.
        PERSONAL_DATA_DB_HOST (str): Database host, default 'localhost'.
        PERSONAL_DATA_DB_NAME (str): Database name, required.

    Returns:
        MySQLConnection: A connection object to the MySQL database.
    """
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    dbname = os.getenv('PERSONAL_DATA_DB_NAME')

    if dbname is None:
        raise ValueError("The PERSONAL_DATA_DB_NAME environment\
                         variable is required.")

    try:
        db_conn = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=dbname
        )
        return db_conn
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        raise
