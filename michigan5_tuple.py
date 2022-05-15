name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
dic=dict()
for line in handle:
    words=line.split()
    if len(words)<1 or words[0]!="From":
        continue
    pieces=words[5].split(":")
    dic[pieces[0]]=dic.get(pieces[0],0)+1
lst=sorted([(k,v) for k,v in dic.items()])
for k,v in sorted(lst):
    print(k,v)