import logging
from datetime import datetime
import threading
import readConfig
import os

class Log:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.patn.join(proDir,"result")
        # 如果文件不存在的话创建文件
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file if it doesn't exist
        logPath = os.path.join(resultPath,str(datetime.now().strftime("%Y%m%d%H%M%S")))
        # create test result file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)
        # defined handler
        handler = logging.FileHandler(os.path.join(logPath,"output.log"))
        # defined formatter
        formatter = logging.Formatter('%(asctime)s = %(name)s - %(levelname)s - %(message)s')
        # defined formatter
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)

class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return  MyLog.log


