# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
read_fh=fh.read().rstrip()

print(read_fh.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
plus=0
count=0
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    bgn=line.find(" ")
    line=line[bgn+1:]
    plus=plus+float(line)
    count=count+1
print("Average spam confidence:",plus/count)