import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

name=input("Enter-")
count=0
while True:
    url=name
    html=urllib.request.urlopen(name).read()
    data=BeautifulSoup(html,"html.parser")
    # print(type(data))

    tags=data.find_all("a")
    # tags=data("a")
    # print(tags)
    lst=list()
    for tag in tags:
        lst.append(tag.get("href",None))
        # print(lst[17])

    count=count+1
    name=lst[17]
    if count==7:
        break
print(re.findall("by_(.+)\.html",lst[17])[0])
# print(lst[17])