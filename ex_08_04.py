fname = input('Enter file: ')

try:
    fop= open(fname)
except:
    print('Error')
    quit()

# oriword=[]
# wordlist=[]
# for lx in fop:
#     lx = lx.rstrip()
#     word = lx.split()
#     oriword.extend(word)
#
# if oriword not in wordlist:
#     wordlist.extend(oriword)
#     wordlist.sort()
#
# print(wordlist)

## Answer

my_list = []
for line in fop:
    words = line.split()
    for word in words:
        if word in my_list:
            continue
        my_list.append(word)

print(sorted(my_list))
