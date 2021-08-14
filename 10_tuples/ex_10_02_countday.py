fname = input('Enter a file name:')

fop = open(fname)

daycount = dict()

for line in fop:
    line = line.rstrip()
    words = line.split()

    if len(words)<3 or words[0]!= 'From':
        continue
    else:
        timepos = words[5].find(':')
        timedot = words[5][:timepos]
        daycount[timedot] = daycount.get(timedot,0)+1

timelist = list()

for k,v in daycount.items():
    timelist.append((k,v))

timelist.sort()

for k,v in timelist[:]:    #这个code用到多个for 是 ok的 ； 注意 list的for 和 dict for循环不一样
    print(k,v)
