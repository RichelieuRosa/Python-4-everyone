fname = open('mbox.txt')
import string

count = 0
wordlist =dict()
letterlist=list()

print('Computing...')

for line in fname:
    line = line.rstrip()
    line = line.translate(str.maketrans('','',string.digits))
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower() #the above three delete all punc/dig/capitalized
    words = line.split()
    print(words)
    for word in words:
        for letter in word:  #search all letter in all words
            count = count +1
            wordlist[letter] = wordlist.get(letter,0) +1

for k,v in wordlist.items():
    letterlist.append((v/count,k))

letterlist.sort(reverse = True)

for k,v in letterlist:
    print(k,v)
