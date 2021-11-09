import os
import requests



print(os,path.isfile("ryw.html"))
file=open('ryw.html','w',encoding='UTF-8')

file.write("<html><head><title>테스트</title></head><body>Hello CICD</body></html>") 
file.close()


URL='127.0.0.1:5000'
response=requests.get(URL)
response.status_code


