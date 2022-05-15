data=open("regex_sum_1541749.txt")
lst=list()
for line in data:
    nums=re.findall("[0-9]+",line)
    for num in nums:
        lst.append(num)
# print(lst)
total=0
for number in lst:
    total = total + int(number)
print(total)