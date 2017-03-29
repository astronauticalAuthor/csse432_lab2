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

def iWant(connectionSocket, command):
    print(command)
    file = open('store/' + command, 'rb')
    l = file.read(1024)
    while l:
        print(l)
        connectionSocket.send(l)
        l = file.read(1024)
    file.close
    connectionSocket.send('EOF')
    connectionSocket.shutdown(SHUT_WR)


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
            if not os.path.isfile(sentence.split(' ')[1]):
                connectionSocket.send('Failure: What you talkin\' bout Willis? I ain\'t seen that file nowhere!')
            else:
                iWant(connectionSocket, sentence.split(' ')[1])    
        else:
            #error
            print('error')
        connectionSocket.send('Thank you for using dickbut')
        connectionSocket.close()
