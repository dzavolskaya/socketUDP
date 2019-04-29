# UDP socket
## Simple socket UDP protocol client and server programs
The programs have to be launched simultaneously in order to communicate with each other.

Socket connection is made through UDP protocol. User enters a message which is transformed based on the defined algorithm: the client splits the string S, assumed to be of length n, into two strings S1 and S2 that are of equal length n/2 if n is even, or of lengths (n + 1)/2 and (n − 1)/2 respectively if n is odd. 
These two distinct strings are sent separately to the server as two UDP packets. Server concatenates S2 to S1 and sends to the client. A verification is done once the client receives the response from the server: divided message originally sent is concatenated inversely as S2S1 and is compared with the received message from the server.

Whether they are equal or not, an appropriate information about result is displayed on the screen.
