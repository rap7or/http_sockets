import socket
from urlparse import urlparse
import urllib
class sock:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.s.connect((host, port))
    
    def post(self, url, params={}):
        url_parsed = urlparse(url)
        params_formatted = urllib.urlencode(params)

        header = 'POST {} HTTP/1.1\r\n'.format(url_parsed.path)
        header += 'Host: {}\r\n'.format(url_parsed.netloc)
        header += 'Content-Type: application/x-www-form-urlencoded\r\n'
        header += 'Content-Length: {}\r\n\r\n'.format(len(params_formatted))
        header += params_formatted + '\r\n'

        self.s.sendall(header)
        return self.s.recv(2048)
        
    def get(self, url, params={}):
        url_parsed = urlparse(url)
        params_formatted = urllib.urlencode(params)
        if len(params) != 0:
            data = '?' + params_formatted
        else:
            data = ''
        header = 'GET {} HTTP/1.1\r\n'.format((url_parsed.path) + (data))
        header += 'Host: {}:{}\r\n'.format(self.HOST, self.PORT)
        header += '\r\n'
        self.s.sendall(header)
        print(header)
        return self.s.recv(2048)
    def close(self):
        self.s.shutdown(socket.SHUT_RDWR)
        self.s.close()