from socket import *
import os.path
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while 1:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)
    if sentence.split(' ')[0] == 'uTake':
        #accept sent file
        file = open('store/' + sentence.split(' ')[1].split(';')[0], 'wb')
        l = sentence.split(';')[1]
        while l:
            file.write(l)
            l = connectionSocket.recv(1024)
        file.close()
        print('recieved file {0}'.format(sentence.split(' ')[1]))
    elif sentence.split(' ')[0] == 'iWant':
        #find file or say file not found
        if not os.path.isfile(sentence.split(' ')[1]):
            connectionSocket.send('Failure: What you talkin\' bout Willis? I ain\'t seen that file nowhere!')
        else:
            file = open('store/' + sentence.split(' ')[1], 'rb')
            l = file.read(1024)
            while l:
                connectionSocket.send(l)
                l = file.read(1024)
            file.close
            connectionSocket.send('EOF')
        print('not implemented')
    else:
        #error
        print('error')
    connectionSocket.send('Thank you for using dickbut')
    connectionSocket.close()
