# -*- coding: utf-8 -*-
import socket
import random

#Configurando o cliente para troca de mensagens em UDP (SOCK_DGRAM)
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp

#Definindo o IP do servidor
IP = '127.0.0.1'

#Definindo a porta para a troca de mensagens com o servidor
porta = 5002

#Definindo o tamanho do buffer para as mensagens
buffer_size = 1024

#Configurando o endereço e porta de destino (servidor)
dest = (IP, porta)

def main():
	#Definindo mensagem para ser enviada ao servidor (Simulação de medida de Temperatura de um sensor)
	msg = round(random.uniform(1, 128), 2)

	#Avisando ao servidor que esse cliente é o sender
	cliente.sendto("s", dest)

	#Enviando mensagem para o servidor
	cliente.sendto(str(msg), dest)

	print( cliente.recv(buffer_size) )

	#Finalisando cliente
	cliente.close()

if __name__ == '__main__':
    main()