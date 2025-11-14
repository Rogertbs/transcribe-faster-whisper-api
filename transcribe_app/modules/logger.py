import os
import logging
import traceback
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

LOG_LEVEL = os.getenv('LOG_LEVEL') or 'DEBUG'
LOG_FILE_LEVEL = os.getenv('LOG_FILE_LEVEL') or 'NONE'

# setup logger
logger = logging.getLogger('transcribe')
logger.setLevel(LOG_LEVEL)

# setup error_logger
error_logger = logging.getLogger('transcribe-error')
error_logger.setLevel(logging.ERROR)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# STDOUT Handler
ch = logging.StreamHandler()
ch.setLevel(LOG_LEVEL)
ch.setFormatter(formatter)
logger.addHandler(ch)

if LOG_FILE_LEVEL != 'NONE': # Log Files config
    # Log File Handler
    lf = RotatingFileHandler('/var/log/transcribe.log', maxBytes=10485760, backupCount=20, encoding='utf8')
    lf.setLevel(LOG_FILE_LEVEL)
    lf.setFormatter(formatter)
    logger.addHandler(lf)

    # Log Error Handler
    lf = RotatingFileHandler('/var/log/transcribe-error.log', maxBytes=10485760, backupCount=20, encoding='utf8')
    lf.setLevel(logging.ERROR)
    lf.setFormatter(formatter)
    error_logger.addHandler(lf)


def log_info(text):
    logger.info(text)

def log_debug(text, params={}):
    logger.debug(f'{text} >> {str(params)}')

def log_error(text, exception):
    error_logger.error(f'{text} >> {exception}')

def log_endpoint_call(endpoint_name, params={}):
    logger.debug(f'{endpoint_name} >> {str(params)}')

def log_endpoint_error(endpoint_name, exception, params={}):
    error_logger.error(f'{endpoint_name} >> {str(params)} >> {str(exception)}\n{traceback.format_exc()}')

