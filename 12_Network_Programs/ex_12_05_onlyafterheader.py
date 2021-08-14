import socket

webname = input('Enter the website URL: ')

HOST = webname.split('/')[2]

POST = 80

myweb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myweb.connect((HOST,POST))
cmd = 'GET '+ webname + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
myweb.send(cmd)

data = myweb.recv(512)
message = data.decode()

header_end_pos = message.find('\r\n\r\n') + 4 #find the end of header
#four chars for \r\n\r\n
print(message[header_end_pos:],end = '')  

while True:
    data = myweb.recv(512)
    if len(message)<1:
        break
    print(data.decode(),end='')

myweb.close()
