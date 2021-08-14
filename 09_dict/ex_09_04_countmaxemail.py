fname = input('Enter a file name: ')

try:
    fop = open(fname)
except:
    print('Not a valid file name')
    quit()



addcount = dict()

for line in fop:
    line = line.rstrip()
    words = line.split()

    if len(words)<3 or words[0]!='From':
        continue
    else:
        addcount[words[1]] = addcount.get(words[1],0) +1

MaxV = None
MaxNum = -1

# for k,v in addcount.items():
#     if MaxV is None:
#         MaxV = k
#         MaxNum = v
#     elif v>MaxNum:
#         MaxV = k
#         MaxNum = v

for add in addcount:
    if addcount[add] > MaxNum:
        MaxNum = addcount[add]
        MaxV = add


print(MaxV, MaxNum)
