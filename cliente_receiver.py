# -*- coding: utf-8 -*-
import socket
import random

#Configurando o cliente para troca de mensagens em UDP (SOCK_DGRAM)
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp

#Definindo o IP do cliente
IP = '127.0.0.1'

#Definindo a porta para a troca de mensagens com o servidor
porta = 5002

#Imprimindo um menu para a seleção da opção
print("\n A. Média\n B. Mediana\n C. Moda\n")

#Definindo a mensagem escolhida pelo cliente
msg = raw_input("Opção: ")

#Conectando cliente com o servidor
cliente.connect((IP,porta))

#Enviando mensagem para o servidor
cliente.send((msg))

#Obtendo resultado enviado pelo servidor
data = cliente.recv(1024)
print(data)

#Finalisando cliente
cliente.close()