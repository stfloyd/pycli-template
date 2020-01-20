"""
Helper functions and definitions for project logging. 
"""

import sys
import logging
from logging.handlers import (
    SMTPHandler, RotatingFileHandler
)

from app import settings


# -----------------------------------------------------------------------------

# Provide a class to allow TLS connection for mail handlers by overloading the emit() method
class TLSSMTPHandler(SMTPHandler):
    def emit(self, record):
        """
        Overwrite the logging.handlers.SMTPHandler.emit function with SMTP_SSL.
        Emit a record.
        Format the record and send it to the specified addressees.
        """
        try:
            import smtplib
            from email.utils import formatdate
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port, timeout=180)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (self.fromaddr, ", ".join(self.toaddrs), self.getSubject(record), formatdate(), msg)
            smtp.ehlo()
            smtp.starttls()
            if self.username:
                smtp.ehlo()
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


# -----------------------------------------------------------------------------
# Logging Configuration

def create_file_handler(level, filename, formatter):
    """
    Helper function for get_logger.
    Creates a file handler for file logging output.
    """

    # handler = logging.FileHandler(
    #     filename=filename,
    #     encoding="utf-8", mode="w"
    # )
    handler = RotatingFileHandler(
        filename,
        maxBytes=settings.LOG_FILE_MAX_KB*1000,
        backupCount=settings.LOG_BACKUP_COUNT
    )
    handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


def create_stream_handler(level, stream, formatter):
    """
    Helper function for get_logger.
    Creates a stream handler for console logging output.
    """

    handler = logging.StreamHandler(stream)
    handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


def create_smtp_handler(level,
                        mailhost, credentials,
                        fromaddr, toaddr,
                        subject,
                        formatter):
    """
    Helper function for get_logger.
    Creates a TLS SMTP handler for email logging output.
    """

    handler = TLSSMTPHandler(
        mailhost=mailhost,
        credentials=credentials,
        secure=(),
        fromaddr=fromaddr, 
        toaddrs=toaddr,
        subject=subject,
        timeout=180
    )
    handler.setLevel(level)
    handler.setFormatter(formatter)
    return handler


# STEAM LOGGERS FORMAT (tuple/list):
# format:
# 0         1 
# level     filepath
# 
# SMTP LOGGERS FORMAT (tuple/list):
# format:
# 0         1           2               3               4
# level     mailhost    credentials     from address    to address
def get_logger(name=__name__,
               stream_loggers=settings.STREAM_LOGGERS,
               file_loggers=settings.FILE_LOGGERS,
               smtp_loggers=settings.SMTP_LOGGERS,
               log_fmt=settings.LOG_FMT,
               time_fmt=settings.LOG_TIME_FMT):
    """
    Create a logger of a given name.
    """

    # Handle verbosity
    console_level = logging.DEBUG

    # Get our logger.
    logger = logging.getLogger(name)
    logger.setLevel(console_level)

    # Create our log formatter.
    formatter = logging.Formatter(
        log_fmt, time_fmt
    )

    for fl in file_loggers:
        handler = create_file_handler(
            level=fl[0],
            filename=fl[1],
            formatter=formatter
        )

        logger.addHandler(handler)
    
    for sl in stream_loggers:
        handler = create_stream_handler(
            level=sl[0],
            stream=sl[1],
            formatter=formatter
        )

        logger.addHandler(handler)

    if settings.SMTP_LOGGING_ENABLED:
        for el in smtp_loggers:
            handler = create_smtp_handler(
                level=el[0],
                mailhost=el[1],
                credentials=el[2],
                fromaddr=el[3],
                toaddr=el[4],
                subject=el[5],
                formatter=formatter
            )

            logger.addHandler(handler)

    # Add a new level to the logger: success
    logging.SUCCESS = 25  # between INFO and WARNING
    logging.addLevelName(
        logging.SUCCESS,
        'SUCCESS'
    )

    # Add a new level to the logger: failure
    logging.FAILURE = 35  # between WARNING and ERROR
    logging.addLevelName(
        logging.FAILURE,
        'FAILURE'
    )

    # Bind a success attr to the logger to log with success level.
    setattr(
        logger,
        'success',
        lambda message, *args: logger._log(logging.SUCCESS, message, args)
    )

    # Bind a failure attr to the logger to log with failure level.
    setattr(
        logger,
        'failure',
        lambda message, *args: logger._log(logging.FAILURE, message, args)
    )

    return logger