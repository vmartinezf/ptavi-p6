#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
if len(sys.argv) != 3: 
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
try:
    METHOD = sys.argv[1]
    line_parameters = sys.argv[2]
    LOGIN = line_parameters.split('@')[0] + '@'
    linea_2parameters = line_parameters.split('@')[1]
    IPSERVER = line_2parameters.split(':')[0]
    PORT = int(line_2parameters.split(':')[1])
except:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
if PORT < 1024:
    sys.exit("ERROR: PORT IS INCORRECT")

# Contenido que vamos a enviar
Line_sip = " sip:" + LOGIN + IP + " SIP/2.0\r\n"
if METHOD == 'INVITE':
    LINE = "INVITE" + Line_sip
elif METHOD == "BYE":
    LINE = "BYE" + Line_sip
    

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
