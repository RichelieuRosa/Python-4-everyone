import urllib.request, urllib.parse, urllib.error

url = 'http://data.pr4e.org/romeo.txt'

urlop = urllib.request.urlopen(url)

chars = 0
limit = 25

for line in urlop:
    line = line.decode()
    nextcount = chars + len(line)
    if nextcount<=limit:  #如果这一行没超过字数，显示这一整行
        print(line.rstrip('\n'))
    elif chars<limit:   #如果超过字数，测试这一行可以显示多少
        char_remain = limit - chars
        leftline = line[:char_remain]  #这一行只显示到char_remain字符位置 注意从0开始算
        print(leftline)
        print(len(leftline))
    chars = nextcount

print(chars)
