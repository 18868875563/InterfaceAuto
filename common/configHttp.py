from urllib import request
import requests
import readConfig as readConfig
from common.Log import MyLog as Log
localReadConfig = readConfig.ReadConfig()

class configHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.header = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_header(self, header):
        self.header = header

    def set_params(self,params):
        self.params = params

    def set_data(self,data):
        self.data = data

    def set_files(self, files):
        self.files = files

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url,param=self.params,headers=self.header,
                                    timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None
    # defined http post method
    def post(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None






