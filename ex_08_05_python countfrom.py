fname = 'mbox-short.txt'

try:
    fop = open(fname)
except:
    print("Error")
    quit()

count = 0
for line in fop:
    line = line.rstrip()
    word = line.split()
    if len(word)<3:
        continue
    if word[0] == 'From':
        if word[1] is ':':
            continue
        count = count+1
        print(word[1])

print('There were', count,'lines in the file with From as the first word')
