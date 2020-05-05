import logging
import time
import datetime as dt

logger = logging.getLogger("robo")
fmt = '%(asctime)s.%(msecs)03d %(process)d %(processName)s %(name)s %(levelname)s %(lineno)s %(filename)s %(funcName)s %(type)s %(message)s'
log_file_name = "log/exness.%d.log" % (int(time.time()),)
logging.Formatter.converter = time.gmtime
logging.basicConfig(level='DEBUG', filename=log_file_name,
                    format=fmt, datefmt='%H:%M:%S')
