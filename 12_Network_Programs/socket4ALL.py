import socket

webname = input('Enter the website URL: ')
# try:
#     webname =
# except:
#     print('Not a valid input')
# http://data.pr4e.org
HOST = webname.split('/')[2]
print(HOST)
POST = 80

myweb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myweb.connect((HOST,POST))
cmd = 'GET '+ webname + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
myweb.send(cmd)

while True:
    data = myweb.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end='')

myweb.close()
