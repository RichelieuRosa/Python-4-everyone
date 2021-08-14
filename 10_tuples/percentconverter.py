def main():
    while True:
        num = input('Please enter a number:')

        try:
            number = float(num)
        except:
            print('Not a valid number')
            quit()

        if number<0:
            print('Not a valid number')
        elif number<1:
            print('Do you want to input a percentage or a real number?')
        else:
            percent = number/100
            print(percent)
            continue

# main()


##

num = input('Please enter a number:')

try:
    number = float(num)
except:
    print('Not a valid number')
    quit()

if number<0:
    print('Not a valid number')
elif number<1:
    print('Do you want to input a percentage or a real number?')
else:
    percent = number/100
    print(percent)
