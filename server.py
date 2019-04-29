#!/usr/bin/env python3

import socketserver
class MyUDPHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        s1 = self.request[0].decode()
        print("==> s1 is: " + s1)
        s2 = self.request[1].recv(1024).decode()
        print("==> s2 is: " + s2)
        received = s2+s1
        print("==> received s2s1 is: " + received)
        self.request[1].sendto(received.encode(),self.client_address)
if __name__ == "__main__":
    HOST, PORT = "localhost", 5555
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
