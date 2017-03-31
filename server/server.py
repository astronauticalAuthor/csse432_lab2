from socket import *
import os.path

def uTake(connectionSocket, command):
    filename = command.split(';')[0].split('/')[-1]
    file = open('store/' + filename, 'wb')
    l = command.split(';')[1]
    while l:
        file.write(l)
        l = connectionSocket.recv(1024)
    file.close()
    print('received file {0}'.format(filename))

def iWant(connectionSocket, filename):
    file = open(filename, 'rb')
    l = file.read(1024)
    while l:
        connectionSocket.send(l)
        l = file.read(1024)
    file.close
    print('sent file {0}'.format(filename))


if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')
    while 1:
        connectionSocket, addr = serverSocket.accept()

        sentence = connectionSocket.recv(1024)
        if sentence.split(' ')[0] == 'uTake':
            #accept sent file)
            uTake(connectionSocket, sentence.split(' ')[1])
        elif sentence.split(' ')[0] == 'iWant':
            #find file or say file not found
            filename = 'store/' + sentence.split(' ')[1]
            if not os.path.isfile(filename):
                connectionSocket.send('Failure: What you talkin\' bout Willis? I ain\'t seen that file nowhere!')
            else:
                iWant(connectionSocket, filename)    
        else:
            #error
            print('error')
        connectionSocket.close()
