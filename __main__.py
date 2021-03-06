#!/usr/bin/python3

from http.server import HTTPServer

from handler import PlayerRequestHandler

def main():
    try:
        server_address = ('', 8888)
        httpd = HTTPServer(server_address, PlayerRequestHandler)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('')
        httpd.socket.close()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
