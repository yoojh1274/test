import os
import requests
import json


print(os.path.isfile("ryw.html"))
file=open('ryw.html','w',encoding='UTF-8')

file.write("<html><head><title>테스트</title></head><body>Hello CICD</body></html>") 
file.close()


value='1234'
params={'code':value}
URL='http://3.112.213.226:8080'
response=requests.get(URL, params=params)
print(response.status_code)
print(response.url)
#print(response.json())


response=requests.post(URL, data=params)
print(response.status_code)
print(response.url)
#print(response.text)



#params={'key':'value'}
#stream = os.popen('curl -s ifconfig.me')
#URL = stream.read()
#reponse=requests.get("http://"+URL+":8080")
#print(reponse.status_code)


