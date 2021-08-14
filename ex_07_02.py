fname = input('Enter the file name: ')

strcri='X-DSPAM-Confidence:'

try:
    fop = open(fname)
except:
    print(fname, 'is not a file')
    quit()

count =0
total =0    #initialize variables

for lx in fop:
    if lx.startswith(strcri):
        count = count+1
        numpos = lx.find(':')
        num = lx[numpos+1:].strip()
        spamc = float(num)
        total = total + spamc

average = total/count

print('Average spam confidence: ', average)
