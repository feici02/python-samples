import mylogger
import mod1
import mod2

if __name__ == '__main__':
    mylogger.mylogger.debug('debug in main')
    mylogger.mylogger.info('info in main')
    mylogger.mylogger.warning('warning in main')
    mylogger.mylogger.error('error in main')
    mylogger.mylogger.critical('critical in main')

    mod1.hi()
    mod2.hi()