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
	#Avisando ao servidor que esse cliente é o receiver
	cliente.sendto("r", dest)

	#Recebendo o menu de escolhas do servidor
	menu = cliente.recv(buffer_size)
	print(menu)
	
	#Obtendo a escolha do cliente
	msg = raw_input()
	msg = msg.lower()

	#Enquanto a mensagem for diferente de X
	while msg != 'x':
		#Enviando mensagem para o servidor
		cliente.sendto(msg, dest)

		#Obtendo resultado enviado pelo servidor
		data = cliente.recv(buffer_size)
		print(data)

		#Avisando ao servidor que esse cliente é o receiver
		cliente.sendto("r", dest)

		#Recebendo o menu de escolhas do servidor
		cliente.recv(buffer_size)
		
		#Obtendo a escolha do cliente
		msg = raw_input()
		msg = msg.lower()

	#Enviando opção de saida
	cliente.sendto( msg, dest )
	print( cliente.recv(buffer_size) )

	#Finalizando cliente
	cliente.close()

	exit()

if __name__ == '__main__':
    main()