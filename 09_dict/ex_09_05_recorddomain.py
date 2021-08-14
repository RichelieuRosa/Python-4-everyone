fop = 'mbox-short.txt'

try:
    fop = open(fname)
except:
    print('Not a valid file')

dom = dict()

for line in fop:
    line = line.rstrip()
    words = line.split()

    if len(words)<3 or words[0]!='From':
        continue
    else:
        atpos = words[1].find('@')    # 注意这里可以直接用分离的字符中查找位置 默认是string格式
        domain = words[1][atpos+1:]
        dom[domain] = dom.get(domain,0)+1

print(dom)
