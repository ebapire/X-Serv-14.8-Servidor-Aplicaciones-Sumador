#!/usr/bin/python


import socket


class webApp:

    def parse(self, request):
        number = int(request.split()[1][1:])
        return number

    def process(self, parsedRequest):

        return ("200 OK", "<html><body><h1>It works!</h1></body></html>")

    def sum(self, number1, number2):
        return number1 + number2

    def __init__(self, hostname, port):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))
        mySocket.listen(5)

        Primer = None;
        try:
            while True:
                print 'Waiting for connections'
                (recvSocket, address) = mySocket.accept()
                print 'Request received'
                peticion = recvSocket.recv(2048)
                print peticion
                print 'Answering back...'
                if Primer == None:
                    try:
                        Primer = self.parse(peticion)
                        print 'Numero recibido:' + str(Primer)
                    except ValueError:
                        None
                    html = "<html><body><h1>Dame otro numero</h1> </p> </body></html>"
                else:
                    try:
                        Segundo = self.parse(peticion)
                        print 'Numero recibido:' + str(Segundo)
                        Suma = self.sum(Primer, Segundo)
                        html = '<html><body><h1>La suma es <b>' + str(Suma) + ' </b> </h1> </p> </body></html>'
                        Primer = None
                    except ValueError:
                        None
                respuesta = "HTTP/1.1 200 OK\r\n\r\n" + html + "\r\n"
                recvSocket.send(respuesta)
                recvSocket.close()
        except KeyboardInterrupt:
            print "Closing binded socket"
            mySocket.close()


if __name__ == "__main__":
    testWebApp = webApp("localhost", 1234)
