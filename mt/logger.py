import logging
import time
import datetime as dt


class MyFormatter(logging.Formatter):
    converter = dt.datetime.fromtimestamp

    def formatTime(self, record, datefmt=None):
        ct = self.converter(record.created)
        if datefmt:
            s = ct.strftime(datefmt)
        else:
            t = ct.strftime("%Y-%m-%d %H:%M:%S")
            s = "%s,%03d" % (t, record.msecs)
        return s


#logger = logging.getLogger(__name__)
logger = logging.getLogger("robo")
# logger.setLevel(logging.DEBUG)
#console = logging.StreamHandler()
# logger.addHandler(console)
fmt = '%(asctime)s.%(msecs)03d %(process)d %(processName)s %(name)s %(levelname)s %(lineno)s %(filename)s %(funcName)s %(type)s %(message)s'
log_file_name = "log/exness.%d.log" % (int(time.time()),)
logging.basicConfig(level='DEBUG', filename=log_file_name,
                    format=fmt, datefmt='%H:%M:%S')
#datefmt = '%Y-%m-%d %H:%M:%S'
#datefmt = '%H:%M:%S'
# logging.basicConfig(filename=log_file_name)
# formatter = MyFormatter(
#    fmt='%(asctime)s %(process)d %(processName)s %(name)s %(levelname)s %(lineno)s %(filename)s %(funcName)s %(type)s %(message)s', datefmt='%H:%M:%S.%f')
#formatter = MyFormatter(fmt='%(asctime)s %(message)s')
# console.setFormatter(formatter)
# logging.basicConfig(filename=log_file_name)
# logging.basicConfig(level='DEBUG', filename=log_file_name,
#                    format=fmt, datefmt=datefmt)
