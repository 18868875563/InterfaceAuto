import  unittest
import requests
from urllib import parse
from time import sleep

class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url='https://www.sojson.com/blog/305.html'

    def test_weather_beijing(self):
        data = {'city':'北京'}
        city = parse.urlencode(data).encode('utf-8')
        r = requests.get(self.url,params=city)
        result = r.json()

        self.assertEquals(result['status'],200)
        self.assertEquals(result['message'],'Success!')
        sleep(3)

    def tesr_weather_param_error(self):
        data ={'city':'999'}
        r = requests.get(self.url,params=data)
        result = r.json()

        self.assertEquals(result['message'],'error')
        sleep(3)

    def test_weather_no_param(self):
        r = requests.get(self.url)
        result = r.json()

        self.assertEquals(result['message'],'error')
        self.assertEquals(result['status'],400)
        sleep(3)


if __name__ == '__main__':
    unittest.main()
