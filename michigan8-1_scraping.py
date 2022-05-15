import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
url=input("Enter -")
html=urllib.request.urlopen(url)
# print(html)

data=BeautifulSoup(html,"html.parser")
spans=data("span")

count=0
total=0
for span in spans:
    # new_span=span.decode()
    # num=re.findall("[0-9]+",new_span)[0]
    num=span.contents[0]
    #num=span.text
    # print(num)
    count=count+1
    total=total+int(num)
print(total)
        

