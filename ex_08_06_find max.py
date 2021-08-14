num_list=[]
num = 0

while True:
    numinp = input('Enter a number: ')
    if numinp == 'done':
        break
    try:
        num = float(numinp)
    except:
        print('WTF did you enter?')
        continue

    if num not in num_list:
        num_list.append(num)

    continue

if num_list: #'if num_list:''    is equal to 'if len(num_list)!=0'
    print('Maximum: ', max(num_list,default = None))
    print('Minimum: ', min(num_list,default = None))
else:
    print('兄弟你啥也没输让我算个啥啊')
