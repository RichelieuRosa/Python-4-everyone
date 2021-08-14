fname = open('words.txt')

wordlist = dict()

count = 0

for line in fname:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count = count+1
        if word in wordlist:
            continue
        wordlist[word] = count

if 'the' in wordlist:
    print('True')
else:
    print('False')

for k,v in wordlist.items():
    print(k, v)
