from socket import *
def iWant(clientSocket, command):
    clientSocket.send(command)
    file = open('receive/'+command.split(' ')[1], 'wb')
    l = clientSocket.recv(1024)
    if l == 'Failure: What you talkin\' bout Willis? I ain\'t seen that file nowhere!':
        print(l)
        l = None
    lastTime = False
    while l and not lastTime:
        if 'EOF' in l:
            lastTime = True
            l = l[:l.index('EOF')]
        file.write(l)
        l = clientSocket.recv(1024)
    file.close()

def uTake(clientSocket, command):
    #send file to server
    clientSocket.send(command+';')
    filename = command.split(' ')[1]
    file = open(filename, 'rb')
    l = file.read(1024)
    while l:
        clientSocket.send(l)
        l = file.read(1024)
    file.close()
    clientSocket.shutdown(SHUT_WR)

if __name__ == '__main__':
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    command = raw_input('Input command:')
    if 'iWant' in command:
        #send to server
        iWant(clientSocket,command)
    elif 'uTake' in command:
        uTake(clientSocket, command)
    else:
        #error
        print('Failure: What you talkin\' bout Willis?')
    modifiedcommand = clientSocket.recv(1024)
    print('From Server:', modifiedcommand)
    clientSocket.close()
