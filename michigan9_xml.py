import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
url="http://py4e-data.dr-chuck.net/comments_1541753.xml"
data=urllib.request.urlopen(url).read()
# print(type(data))
# print(type(data.decode()))

tree = ET.fromstring(data)
# print(tree.findall("comments/comment/count"))
lst = tree.findall("comments/comment/count")
total = 0
for item in lst:
    total = total + int(item.text)
print(total)
