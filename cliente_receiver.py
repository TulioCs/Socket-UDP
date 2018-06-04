# -*- coding: utf-8 -*-

import socket
import random

cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp
IP = '127.0.0.1'
#IP = '192.168.43.171'
porta = 5002
cont = 0
#while True:
print("A. Média\n B. Mediana\n C. Moda\n")

msg = raw_input("Opção: ")

cliente.connect((IP,porta))

cliente.send((msg))

data = cliente.recv(1024)

print(data)
