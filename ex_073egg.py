fname = input('Enter the file name: ')

try:
    fop = open(fname)
except:
    if fname == 'na na boo boo':
        print("You have been punk'd!")
        quit()
    else:
        print('File cannot be opened: ', fname)
        quit()

count = 0

for lx in fop:
    if lx.startswith('Subject:'):
        count = count +1


print('There were ', count, ' subject lines in ', fname)
