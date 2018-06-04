# -*- coding: utf-8 -*-
import socket
import random

#Configurando o cliente para troca de mensagens em UDP (SOCK_DGRAM)
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp

#Definindo o IP do cliente
IP = '127.0.0.1'

#Definindo a porta para a troca de mensagens com o servidor
porta = 5002

#Definindo mensagem para ser enviada ao servidor (Simulação de medida de Temperatura de um sensor)
msg = round(random.uniform(1, 40), 2)

#Conectando cliente com o servidor
cliente.connect((IP,porta))

#Enviando mensagem para o servidor
cliente.send(str(msg))

#Finalisando cliente
cliente.close()