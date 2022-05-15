name = input("Enter file:")
handle = open(name)
counts=dict()
for line in handle:
    words=line.split()
    if len(words)<1 or words[0]!="From":
        continue
    counts[words[1]]=counts.get(words[1],0)+1
bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)