#This program creates an http server without http librarly, only sockets manually
import socket
from multiprocessing import Process
import os


def handle(connection, client_address):
    print('servicing', client_address)

    content=''

    while True:


        #Check if the first data that it receive is a GET with a content
        data = connection.recv(1)

        if data: 
            content += data.decode()
        else:
            break
        #Until the content ends
        if content[-4:] == '\r\n\r\n': break

    path_line = content.split('\n')[0]
    path = path_line.split(' ')[1]
    filename = path.split('/')[-1]

    #mime = 'text/html'

    body = ''

    #handle html file
    if path.endswith('.html'):
        with open(filename) as file:
            body = file.read()

    #handle jpg
    if path.endswith('.jpg'):
        mime = 'img/jpeg'
        with open(filename, 'rb') as file:
            body = file.read()

    #handle python file
    if path.endswith('.py'):
        body = os.popen('python %s' % filename).read()


    if body == '':
        body = '404'

    try:
        body = body.encode()
    except:
        pass

    #HTML format needed to send data
    connection.send(b'HTTP/1.1 200 OK\r\n')
    connection.send('Content-Type: {0}\r\n'.format(mime).encode())
    connection.send('Content-Length: {0}\r\n'.format(len(body)).encode())
    connection.send(b'\r\n')
    connection.send(body)
    connection.send(b'\r\n\r\n')

    connection.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#If use localhost address, you need to reuse it with SO_REUSEADDR
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Does not filter by any specific address with port 8080
sock.bind(('', 8080))
sock.listen(1)

if __name__ == '__main__':
    while True:
        connection, client_address = sock.accept()
        print('acccepted new connection')

        process = Process(target=handle, args=(connection, client_address))
        process.start()