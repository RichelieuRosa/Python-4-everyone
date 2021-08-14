fname = open('mbox-short.txt')

daycount = dict()

# for line in fname:
#     line = line.rstrip()
#     words = line.split()
#     if len(words)<3:
#         continue
#     for word in words:
#         if words[0] != 'From' or word != words[2]:
#             continue
#         daycount[word] = daycount.get(word,0) +1
#
# print(daycount)


# instruction code
for line in fname:
    words = line.split()
    if len(words)<3 or words[0] != 'From':
        continue
    else:
        if words[2] not in daycount:
            daycount[words[2]] = 1
        else:
            daycount[words[2]] += 1

print(daycount)
