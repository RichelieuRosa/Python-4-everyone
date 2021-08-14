import re

fname = open('mbox.txt')

key = input('Enter a regular expression:')
regkey = str(key)

count = 0
for line in fname:
    line = line.rstrip()
    if re.search(regkey,line):
        count = count +1

print("mbox.txt had", str(count), "lines that matched", regkey)

# co=0
# for line in fname:
#     line = line.rstrip()
#     if re.findall(regkey,line)!=[]:
#         co +=1
# print("Algorithm2 result:", co)
