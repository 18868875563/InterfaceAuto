import  requests
from requests.auth import  HTTPBasicAuth
from requests.auth import HTTPDigestAuth
import json

base_url = 'http://httpbin.org'

#r = requests.get(base_url+'/get')
#print(r.status_code)

#r = requests.post(base_url+'/post')
#print(r.status_code)

#r = requests.put(base_url+'/put')
#print(r.status_code)

#r = requests.delete(base_url+'/delete')
#print(r.status_code)

#参数传递
#param_data = {'user':'zxw','password':'6666'}
#r = requests.get(base_url+'/get',params=param_data)
#print(r.status_code)
#print(r.url)

#form_data = {'user':'zxw','password':'6666'}
#r = requests.get(base_url+'/get',data=form_data)
#print(r.text)

#请求头定制
#form_data = {'user':'zxw','password':'6666'}
#header = {'user-agent':'Mozilla/5.0'}
#r = requests.get(base_url+'/get',data=form_data,headers=header)
#print(r.text)
#print(r.json())

#cookie设置
#cookie = {'user':'51zxw'}
#r = requests.get(base_url+'/cookies',cookies=cookie)
#print(r.text)

#获取cookie
#r = requests.get('http://www.baidu.com')
#print(r.cookies)
#print(type(r.cookies))
#for key,value in r.cookies.items():
 #   print(key+':'+value)

#超时时间设置
#cookie = {'user':'51zxw'}
#r = requests.get(base_url+'/cookies',cookies=cookie,timeout=3)
#print(r.text)

#文件上传
#file = {'file': open('', 'rb')}
#r = requests.post(base_url+'/post',files=file)
#print(r.text)

#session
#r = requests.get(base_url+'/cookies/set/user/51zxw')
#print(r.text)

#r = requests.get(base_url+'/cookies')
#print(r.text)
#s = requests.Session()
#r = s.get(base_url+'/cookies/set/user/51zxw')
#print(r.text)

#r = s.get(base_url+'/cookies')
#print(r.text)

#证书验证
#r = requests.get('https://www.12306.com',verify= False)
#print(r.text)

#代理设置
#proxies = {'http':'http://219.141.153.41:80'}
#r = requests.get(base_url+'get',proxies=proxies)
#print(r.text)

#身份认证-BasicAuth
#r = requests.get(base_url+'/basic-auth/51zxw/8888',auth=HTTPBasicAuth('51zxw','8888'))
#print(r.text)

#r = requests.get(base_url+'/digest-auth/auth/zxw/6666',auth=HTTPDigestAuth('zxw','6666'))
#print(r.text)

#流式请求
r = requests.get(base_url+'/stream/10',stream=True)
if r.encoding is None:
    r.encoding='utf-8'

for line in r.iter_lines(decode_unicode=True):
    if line:
        data = json.loads(line)
        print(data['id'])



