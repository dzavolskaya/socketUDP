#!/usr/bin/env python3

import socket

def isEven(num):
    if num % 2 == 0:
        return True

def buildNewMessage(message, startRange, endRange):
    result = ""
    for letter in range(startRange, endRange):
        result += message[letter]
    return result

def splitMessage(message, messageLength):
    if isEven(messageLength):
        m1 = buildNewMessage(message, 0, round(messageLength/2))
        m2 = buildNewMessage(message, round(messageLength/2), messageLength)
    else:
        m1 = buildNewMessage(message, 0, round((messageLength+1)/2))
        m2 = buildNewMessage(message, round((messageLength+1)/2), messageLength)
    return m1, m2

while True:
    s = input("Enter your message to send (press 0 - to Exit): ")
    if (s == "0" or 0):
        print("OK, goodbye!")
        break
    n = len(s)
    s1, s2 = splitMessage(s, n)

    sent = s1+s2
    sentInversed = s2+s1

    HOST = "localhost"
    PORT = 5555
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(s1.encode(),(HOST, PORT))
    client_socket.sendto(s2.encode(),(HOST, PORT))
    received = client_socket.recv(1024).decode()
    print("==> You sent \'" + sent + "\' as two messages: \'" + s1
    + "\' and \'" + s2 + "\'. \n==> Server received: \'" + received +"\'")
    if (sentInversed == received):
        print("Status: OK. All packets fully delivered")
    else:
        print("Status: ERROR. Packets are not delivered as expected")
