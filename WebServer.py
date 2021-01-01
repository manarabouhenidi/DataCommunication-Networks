from socket import *


def main():
    # Prepare a sever socket
    serverSocket = socket(AF_INET, SOCK_STREAM)  # create socket
    serverSocket.bind(('', 80))  # associate port with socket
    serverSocket.listen(1)  # listen for 1 connection

    while True:
        # Establish the connection
        print('Ready to Serve...')  # DEBUG: proof server is ready
        connectionSocket, addr = serverSocket.accept()  # create connection socket for accepted client

        try:
            message = connectionSocket.recv(1024)  # recieve messg
            print(message)  # DEBUG: proof connection is made

            filename = message.split()[1]  # determine filename
            print(filename)  # DEBUG: to check filename
            f = open(filename[1:])  # open the file

            outputdata = f.read()  # outputdata = data in the file requested
            print(outputdata)  # DEBUG: to check outputdata

            # Send one HTTP header line into socket
            connectionSocket.send('\n')
            connectionSocket.send('HTTP/1.1 200 OK\n')
            connectionSocket.send("Connection: close\n")
            # I need to put in the right size and send it out
            LengthString = ('Content - Lenght: ' + str(len(outputdata)) + '\n')
            connectionSocket.send(LengthString)
            connectionSocket.send('Content-Type: text/html\n')
            connectionSocket.send('\n')
            connectionSocket.send('\n')

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):  # for all the output data
                connectionSocket.send(outputdata[i])  # send the data
                connectionSocket.close()  # close connection
        except IOError:  # if IOError
            print('IOError')  # DEBUG: signal error
            # Send response message for file not found
            connectionSocket.send('\n')
            error404 = '404 Not Found: Requested document not found'
            connectionSocket.send(error404)
            connectionSocket.close()  # close connection

    serverSocket.close()
    pass


if __name__ == '__main__':
    main()
