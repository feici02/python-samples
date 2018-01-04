import logging
import logging.config

logging.config.fileConfig('logging.conf')
mylogger = logging.getLogger("mylogger")
