
import inspect
import logging

class LoggingClass:

    @staticmethod
    def log_generator():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D:\\Credence\\Assignments\\My Assignments\\Final Revision\\Interview1\\logs\\Cred.log")
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger




















































