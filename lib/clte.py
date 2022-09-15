import re

#Define some global variables
RN = '\n'

# CL.TE functionality
def PREFIX(HOSTNAME, ACTION, REQUEST_METHOD):
#You can add more HTTP headers for ur purpose
    PREF = "{} /{} HTTP/1.1".format(REQUEST_METHOD, ACTION) + RN 
    PREF += "Host: {}".format(HOSTNAME) + RN
    PREF += "X-Ignore: X" + RN


    if '\r' not in PREF:
        PREF = PREF.replace('\n', '\r\n')

    return PREF
