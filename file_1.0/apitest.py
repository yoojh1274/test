#!/usr/bin/python3
import os
import requests
import logging
import logging.handlers

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG) # 모든 레벨의 로그를 Handler들에게 전달해야 합니다.
formatter = logging.Formatter('%(asctime)s:%(module)s:%(levelname)s:%(message)s', '%Y-%m-%d %H:%M:%S')

params={'key':'value'}
re=requests.get("http://localhost:8080/test/yw.html")
res=requests.get("http://localhost:8080/")
#res=requests.get("http://localhost:8080")

l = [re, res]

for code in l:
    if code == res:
        print('TEST FINISH')
        break
    print(re.status_code)




#####
#params={'key':'value'}
#stream = os.popen('curl -s ifconfig.me')
#URL = stream.read()
#reponse=requests.get("http://"+URL+":8080")
#print(reponse.status_code)

