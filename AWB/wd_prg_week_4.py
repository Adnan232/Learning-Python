# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

import urllib.request
import re
from bs4 import BeautifulSoup


html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1229030.html').read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
tags = soup('span')
for tag in tags:
    y = str(tag)
    x = re.findall("[0-9]+",y)
    for i in x:
        i = int(i)
        sum = sum+i
print(sum)