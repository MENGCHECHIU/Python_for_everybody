fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line=line.rstrip()
    pieces=line.split()
    if len(pieces)<1 or pieces[0]!="From":
        continue
    print(pieces[1])
print("There were 27 lines in the file with From as