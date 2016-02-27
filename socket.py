import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = '127.0.0.1'
port = 80

try:
    s.connect((address, port)) 
except Exception, e:
    print('ERROR connecting to %s:%d :%s' % (address, port, e))
