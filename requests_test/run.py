import unittest
from BSTestRunner import BSTestRunner
import  time

#指定测试用例或者测试报告的路径
test_dir = './test_case'
report_dir = './reports'

#加载用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_weather.py')


now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+'test_report.html'

with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='Weather API Test Report')
    runner.run(discover)