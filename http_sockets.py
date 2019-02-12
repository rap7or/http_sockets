#!/usr/bin/python3
import socket
from urllib.parse import urlparse
from urllib.parse import urlencode
class sock:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        self.s.connect((host, port))
    
    def post(self, url, params={}):
        url_parsed = urlparse(url)
        params_formatted = urlencode(params)

        header = bytes('POST {} HTTP/1.1\r\n'.format(url_parsed.path))
        header += bytes(b'Host: {}\r\n'.format(url_parsed.netloc))
        header += bytes('Content-Type: application/x-www-form-urlencoded\r\n')
        header += bytes('Content-Length: {}\r\n\r\n'.format(len(params_formatted)))
        header += bytes(params_formatted + '\r\n')

        self.s.sendall(header)
        print(self.s.recv(2048))
        #print(header)
    def test():
        return "test"