from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input command:')
if 'iWant' in sentence:
    #send to server
    clientSocket.send(sentence)
    file = open('receive/'+sentence.split(' ')[1], 'wb')
    l = clientSocket.recv(1024)
    if l == 'Failure: What you talkin\' bout Willis? I ain\'t seen that file nowhere!':
        print(l)
        l = None
    while l:
        if 'EOF' in l:
            lastTime = true
            l = l[:l.index('EOF')]
        file.write(l)
        l = clientSocket.recv(1024)
    file.close()
elif 'uTake' in sentence:
    #send file to server
    clientSocket.send(sentence+';')
    filename = sentence.split(' ')[1]
    file = open(filename, 'rb')
    l = file.read(1024)
    while l:
        clientSocket.send(l)
        l = file.read(1024)
    file.close()
    clientSocket.shutdown(SHUT_WR)
else:
    #error
    print('Failure: What you talkin\' bout Willis?')
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence)
clientSocket.close()
