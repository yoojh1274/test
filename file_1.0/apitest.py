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

#<p><img src="https://image.shutterstock.com/image-photo/closeup-portrait-laughing-brunette-girl-600w-1082155934.jpg" alt="smile"/></p>
#<p><img src="https://image.shutterstock.com/image-photo/cracks-on-surface-blue-ice-600w-655427254.jpg" alt="winter"/></p>