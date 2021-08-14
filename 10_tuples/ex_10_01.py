fname = input('Enter a file name: ')

fop = open(fname)

addbook = dict()
for line in fop:
    line = line.strip()
    words = line.split()

    if len(words)<3 or words[0]!= 'From':
        continue
    else:
        addbook[words[1]] = addbook.get(words[1],0)+1

newbook = list()

for k,v in addbook.items():
    newbook.append((v,k))

newbook = sorted(newbook,reverse=True)

for v,k in newbook[:1]:   #注意要用for loop的时候 必须是一组数据 而不是一个数据点
    print(k,v)
