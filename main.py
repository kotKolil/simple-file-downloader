import URIClass
from settings import *
from URIClass import *

import socket
from threading import *
import os


def file_download(URIObject: URIClass) -> int:
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((URIObject.domain, 80))
    request_body = b"GET / %/1.1\r\nHost:%\r\n\r\n" % URIObject.protocol, URIObject.URI
    socket1.sendall(request_body)
    file_data = b""
    while True:
        chunk = socket1.recv(int(BUFFER_SIZE))
        if chunk:
            file_data += chunk
        else:
            break
    if URIClass.path == "/":
        filename = "index"
    else:
        filename = URIClass.path.split("/")[-1]

    with open(os.path.join(os.getcwd(), download_dir, filename), "rb") as file:

        file.write(file_data)
        file.close()

    return 0


while 1:
    URI = input()
    parsed_uri = URIClass(URI)

    t = Thread(target=file_download, args=(parsed_uri,))
    t.start()
    t.join()
