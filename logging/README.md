# logging

## 1. basic usage
The log message is on stdout by default.
```
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("This is a debug message")
logging.info("This is a info message")
logging.error("This is a error message")
```

## 2. log on file
To write the log message to a file, you just need to modify the config line like below:
```
logging.basicConfig(filename="sample.log", level=logging.INFO)
```

## 3. samples
1. [sample1](./sample1)
1. [sample2](./sample2)