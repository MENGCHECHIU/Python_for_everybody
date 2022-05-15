import urllib.request, urllib.parse, urllib.error
import json
url="http://py4e-data.dr-chuck.net/comments_1541754.json"
data=urllib.request.urlopen(url).read()
# print(urllib.request.urlopen(url).read().decode())

info=json.loads(data)
# print(info["comments"])
total=0
for counts in info["comments"]:
    total = total + counts["count"]
print(total)

