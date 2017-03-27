"""
Logger helper class
Logger for Python GVVMC applications
"""

import logging
import zipfile
import os
import time
import glob
import calendar
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


class TimedCompressedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    """
       Extended version of TimedRotatingFileHandler that compress logs on rollover.
       Pending to be tested
    """

    def __init__(self, filename, when='h', interval=1, backupCount=0, encoding=None, delay=0, utc=0, maxBytes=0):
        logging.handlers.TimedRotatingFileHandler.__init__(self, filename, when, interval, backupCount, encoding, delay,
                                                           utc)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.

        we are also comparing times
        """
        if self.stream is None:  # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:  # are we rolling over?
            msg = "%s\n" % self.format(record)
            self.stream.seek(0, 2)  # due to non-posix-compliant Windows feature
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0

    def doRollover(self):
        if self.stream:
            self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        t = self.rolloverAt - self.interval
        time_tuple = time.localtime(t)
        dfn = self.baseFilename + "_" + time.strftime(self.suffix, time_tuple)
        # Must do rotated backup
        if True or self.backupCount > 0:
            cnt = 1
            dfn2 = "%s.%03d.%s" % (dfn, cnt, 'log')
            while os.path.exists(dfn2) or os.path.exists(dfn2 + '.zip'):
                cnt += 1
                dfn2 = "%s.%03d.%s" % (dfn, cnt, 'log')
            os.rename(self.baseFilename, dfn2)

            # Zip file routine
            target_zip = dfn2 + ".zip"
            if os.path.exists(target_zip):
                existing_zips = glob.glob(target_zip)
                os.rename(target_zip, target_zip + "_" + str(len(existing_zips)))
            file = zipfile.ZipFile(target_zip, "w")
            file.write(dfn2, os.path.basename(dfn2), zipfile.ZIP_DEFLATED)
            file.close()
            os.remove(dfn2)
        else:
            if os.path.exists(dfn):
                os.remove(dfn)
            dfn2 = "%s.%s" % (dfn, 'log')
            os.rename(self.baseFilename, dfn2)

        self.stream = open(self.baseFilename, 'w')
        now = datetime.utcnow()
        now = calendar.timegm(now.timetuple())
        self.rolloverAt = now + self.interval


def init_logger(file_path=None, application_name="", is_debug=True, needs_output=True, log_name=None):
    if file_path is None:
        file_path = ""
    else:
        file_path = os.path.join(file_path, './')
        file_path = os.path.abspath(file_path) + "/"

    logger = logging.getLogger((log_name if log_name is not None else None))
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s')

    if needs_output:
        formatter = logging.Formatter(
            '%(asctime)s %(levelname)s [%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s')
        handler = TimedCompressedRotatingFileHandler(file_path + application_name + ".log",
                                                     when="D",
                                                     interval=3,
                                                     maxBytes=8388608)
        handler.setFormatter(formatter)

        if is_debug is True:
            handler.setLevel(logging.DEBUG)
            logger.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.INFO)
            logger.setLevel(logging.INFO)
        logger.addHandler(handler)

    logger.info("Application started at: %s", datetime.utcnow())
    return logger
