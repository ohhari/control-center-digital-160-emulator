# echo-server.py

import socket

xmlConnectionList = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
    <list>
        <item><cpuName>A</cpuName><consoleName>B</consoleName></item>
    </list>
</root>'''
xmlConsoleList = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
    <list>
        <item><name>A</name></item>
    </list>
</root>'''
xmlMatrixList = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
    <list>
        <item><name>Matrix</name></item>
    </list>
</root>'''
xmlConnect = '''<?xml version="1.0" encoding="utf-8"?>
<root>
    <result type="connect">
        Connection successfull
    </result>
</root>'''

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 8080  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                data = data.decode("utf-8")
                print(f"Received Data: \n{data}")
                if not data:
                    break
                if '<connect>' in data:
                    conn.sendall(xmlConnect.encode("utf-8"))
                    print(f"Send Data: \n{xmlConnect}")
                    break
                if '<MatrixConnectionList/>' in data:
                    conn.sendall(xmlConnectionList.encode("utf-8"))
                    print(f"Send Data: \n{xmlConnectionList}")
                    break
                if '<DviConsole/>' in data:
                    conn.sendall(xmlConsoleList.encode("utf-8"))
                    print(f"Send Data: \n{xmlConsoleList}")
                    break
                if '<DviMatrix/>' in data:
                    conn.sendall(xmlMatrixList.encode("utf-8"))
                    print(f"Send Data: \n{xmlMatrixList}")
                    break
        conn.close()
               
