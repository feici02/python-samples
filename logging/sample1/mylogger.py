import logging

logging.config.fileConfig('logging.conf')
mylogger = logging.getLogger("mylogger")

mylogger = logging.getLogger("mylogger")
mylogger.setLevel(logging.INFO)

# create the logging file handler
consoleHandler = logging.StreamHandler()
fileHandler = logging.FileHandler("mylogger.log")

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(me\
ssage)s')

fileHandler.setFormatter(formatter)
consoleHandler.setFormatter(formatter)

# add handler to mylogger object
mylogger.addHandler(fileHandler)
mylogger.addHandler(consoleHandler)