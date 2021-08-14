fname = open('mbox-short.txt')

#question 2 to make code more general
# for lx in fname:
#     lx = lx.rstrip()
#     word = lx.split()
#     if len(word) <3:
#         continue
#     if word[0] != 'From':
#         continue
#
#     print(word[2])

#question 3 using compound

for lx in fname:
    word = lx.split()
    if len(word)<3 or word[0]!='From':
        continue
    print(word[2])
