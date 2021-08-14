# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
# # print('Debug:', words)
#     if len(words) == 0 : continue
#     if words[0] != 'From' : continue
#     print(words[2])

def chop(t):
    #remove 1st and last, returns NONE
    del t[0]
    del t[-1]

def middle(n):
    new = n[1:]
    del new[-1]
    return new

let = ['a','b','c','d']
let2 = ['1a','2b','3c','4d']

chop_att = chop(let)
print(let) #new list
print(chop_att) #None

mid_att = middle(let2)
print(let2) #unchanged
print(mid_att) #result
