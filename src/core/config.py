import os
from logging.config import dictConfig
from pathlib import Path

from dotenv import load_dotenv

load_dotenv('../.env')


class Config:
    # Flask configuration
    # Check this documentation for more information
    # https://flask.palletsprojects.com/en/3.0.x/config/
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.getenv('SECRET_KEY')

    # Custom configuration
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOG_LEVEL = 'DEBUG'
    LOG_HANDLER = ['console', 'file']


LOG_FOLDER = Config.BASE_DIR / '../logs'
LOG_FOLDER.mkdir(parents=True, exist_ok=True)
dictConfig(
    {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
        },
        'handlers': {
            'console': {
                'level': Config.LOG_LEVEL,
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
            'file': {
                'level': Config.LOG_LEVEL,
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'default',
                'filename': LOG_FOLDER / 'file.log',
                'maxBytes': 50000,
                'backupCount': 5,
            },

        },
        'loggers': {
            'log': {
                'handlers': Config.LOG_HANDLER,
                'level': Config.LOG_LEVEL,
                'propagate': True,
            }
        },
    }
)
