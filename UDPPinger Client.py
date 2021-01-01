import socket
from socket import AF_INET, SOCK_DGRAM
import time

print('Running')
serverName = 'www.google.com'
#serverName = '127.0.0.1'  # server set as localhost
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)  # create the socket
clientSocket.settimeout(1)  # sets the timeout at 1 sec
sequence_number = 1  # variable to keep track of the sequence number
rtt = []  # list to store the rtt values

while sequence_number <= 10:
    start = time.time()  # the current time
    message = ('PING %d %d' % (sequence_number, start))  # client message
    clientSocket.sendto(message, (serverName, 12000))  # client sends a message to the server
    try:
        message, address = clientSocket.recvfrom(1024)  # recieves message from server
        elapsed = (time.time() - start)  # calculates the rtt
        rtt.append(elapsed)
        print (message)
        print('Round Trip Time is:' + str(elapsed) + ' seconds')
    except socket.timeout:  # if no reply within 1 second
        print message
        print 'Request timed out'
    sequence_number += 1  # incremented by 1

    if sequence_number > 10:  # closes the socket after 10 packets
        mean = sum(rtt, 0.0) / len(rtt)
        print ''
        print 'Maximum RTT is:' + str(max(rtt)) + ' seconds'
        print 'Minimum RTT is:' + str(min(rtt)) + ' seconds'
        print 'Average RTT is:' + str(mean) + ' seconds'
        print 'Packet loss rate is:' + str((10 - len(rtt)) * 10) + ' percent'
        clientSocket.close()