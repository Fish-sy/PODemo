import time
import logging.config

"""
    打印日志
"""

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "formatter": {
            "format": "[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s"
        }
    },
    # 处理器
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "formatter"
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "formatter",
            "filename": './' + "/data/logs/" + time.strftime('%Y-%m-%d') + ".log",
            "encoding": "utf-8",
            "mode": "w"
        }
    },
    # 记录器
    "loggers": {
        "C": {
            "handlers": ["console"],
            "level": "DEBUG"
        },
        "F": {
            "handlers": ["file"],
            "level": "INFO"
        }
    }
})
