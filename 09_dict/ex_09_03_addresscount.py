fname = open('mbox-short.txt')


addcount = dict()
for line in fname:
    line = line.rstrip()
    words = line.split()

    if len(words)<3 or words[0]!='From':
        continue
    else:
        addcount[words[1]] = addcount.get(words[1],0) +1


print(addcount)
