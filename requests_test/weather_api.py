import requests
from urllib import  parse
import json

#构建接口测试数据
data = {'city':'北京'}
city = parse.urlencode(data).encode('utf-8')
base_url = 'https://www.sojson.com/blog/305.html'

#发送请求

r = requests.get(base_url,params=city)
print(r.text)
response_data = r.json()

print(response_data['code'])
print(response_data['msg'])
#print(response_data['status'])
#print(response_data['city'])
#print(response_data['date'])





