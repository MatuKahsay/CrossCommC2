# CrossCommC2

CrossCommC2 is a Python-based networking tool designed for secure communication and remote administration. It employs sockets for network communication, threading for handling multiple connections, and SSL for secure data transmission. This tool is equipped with features for system persistence, data encoding, and dynamic payload generation.

Disclaimer: This tool is for educational and ethical testing purposes only. The author is not responsible for misuse or illegal activities.
Features

    Secure Socket Layer (SSL) encryption for safe communication.
    Multi-threading support to handle multiple client connections.
    Base64 encoding to ensure safe data transmission.
    Persistence techniques for both Windows and Linux systems.
    Dynamic payload generation for various scenarios.
    PowerShell cradle for remote Windows exploitation.

Installation

    Clone the repository or download the source code.
    Ensure Python 3.x is installed on your system.
    Install required dependencies:

    bash

pip install -r requirements.txt

Generate SSL certificate and key for secure communication (if not already present):

bash

    openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out cert.pem

    Adjust the init_server_socket function's certfile and keyfile paths to your certificate files.

Usage
Server Setup

    Initialize the server socket:

    python

secure_sock = init_server_socket()

Start the listener handler in a separate thread if handling multiple connections:

python

    listener_handler()

Client Commands

    help: Displays the help menu with available commands.
    exit: Safely disconnects the client and shuts down the server.
    background: Moves the current client session to the background.
    persist: Initiates persistence mechanism on the connected client system.

Persistence

    Windows: Copies payload to a public directory and adds a registry entry for autostart.
    Linux: Adds a crontab entry to execute the payload periodically.

Dynamic Payload Generation

    winplant, linplant, exeplant: Generate and customize Python scripts for deployment on respective platforms.

PowerShell Cradle

Generates and encodes a PowerShell command to download and execute payloads remotely.
Security and Disclaimer

This tool incorporates basic encryption and security features. However, it should only be used in a controlled environment, strictly for educational or authorized ethical hacking purposes. Unauthorized use of this tool against systems without explicit permission is illegal and against ethical guidelines.
Contribution

Contributions are welcome. Please submit pull requests or issues through the project's GitHub page.
License

This project is licensed under [LICENSE NAME]. Please see the LICENSE file for more details.