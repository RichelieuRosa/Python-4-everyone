fname = input('Please enter a file name:')

fop = open(fname)

import re

numlist = list()
for line in fop:
    line = line.rstrip()
    num= re.findall('^N.*?: ([0-9]+)',line) #注意 这里输出的是单个数字的list--需要把数字提取出来再import
    if len(num)>0:
        for v in num:
            v = float(v)
            numlist.append(v)

avg = sum(numlist)/len(numlist)
avg = int(avg)

print(avg)
