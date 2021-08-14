import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl
# 用来测试的网站是： https://en.wikipedia.org/wiki/Pulsatile_flow
#ignore SSL certification error (just copy it)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('p')
print(tags)
for tag in tags:
    count +=1

print(count)
