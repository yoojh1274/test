#!/usr/bin/python3
import os
import requests

re=requests.get("http://localhost:80/yw.html")
res=requests.get("http://localhost:80/")

l = [re, res]

for code in l:
    if code == res:
        print('TEST FINISH')
        break
    print(re.status_code)

