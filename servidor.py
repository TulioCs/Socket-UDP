# -*- coding: utf-8 -*-
import socket
from datetime import datetime
import statistics

#Configurando o servidor para transferência via UDP (SOCK_DGRAM)
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp

#Definindo o IP do servidor
IP = '127.0.0.1'

#Definindo a porta
porta = 5002

#Definindo o tamanho do buffer para as mensagens
buffer_size = 1024

#Configurando o servidor com o IP e a porta definidos anteriormente
servidor.bind((IP, porta))

#Função para retornar todas as temperaturas armazenadas no arquivo
def get_dados ():
    #Abrindo o arquivo para leitura
    dados = open('dados.txt','r')

    #Criando uma lista para retornar as temperaturas
    temperatura = []

    #Percorrendo as linhas do arquivo
    for line in dados:
        #Obtendo as temperaturas e as datas e horas
        x , y = line.split(';')
        #Atribuindo os valores das temperaturas (float) para a lista
        temperatura.append(float(x))
    #Fechando o arquivo
    dados.close()

    return temperatura

#Função que calcula a média de uma lista de números
def media (list_tmp):
    return statistics.mean(list_tmp)

#Função que calcula a mediana de uma lista de números
def mediana (list_tmp):
    return statistics.median(list_tmp)

#Função que calcula a moda de uma lista de números
def moda (list_tmp):
    return statistics.mode(list_tmp)

def main():
    while True:
        
        #Obtendo o dado (temperatura / opção) e endereço do cliente
        dado, cliente_endereco = servidor.recvfrom(buffer_size)
        
        #Se a mensagem do cliente foi a opção A
        if (dado == 'A'):
            #Atualizando a lista dos dados
            list_tmp = get_dados()
            #Enviando media para o cliente receptor
            servidor.sendto(str(media(list_tmp)), cliente_endereco)
        
        #Se a mensagem do cliente foi a opção B
        elif(dado == 'B'):
            #Atualizando a lista dos dados
            list_tmp = get_dados()
            #Enviando mediana para o cliente receptor
            servidor.sendto(str(mediana(list_tmp)), cliente_endereco)
        
        #Se a mensagem do cliente foi a opção C
        elif (dado == 'C'):
            #Atualizando a lista dos dados
            list_tmp = get_dados()
            try:
                #Enviando moda para o cliente receptor
                servidor.sendto(str(moda(list_tmp)), cliente_endereco)
            except statistics.StatisticsError:
                #Caso não exista moda
                servidor.sendto("\nNão existe moda", cliente_endereco)
        
        try:
            #Verficando se a variável 'dado' é um float
            float(dado)
            #Abrindo o arquivo para escrita
            dados = open('dados.txt','a')
            #Obtendo a data e hora atual
            now = datetime.now()
            #Escrevendo a leitura do sensor no arquivo
            dados.write(dado)
            #Escrevendo o parâmetro de divisão dos dados
            dados.write(";")
            #Escrevendo a data e hora atual no arquivo
            dados.write(str(now) + "\n")
            #Fechando o arquivo
            dados.close()
        except ValueError:
            #Se a variável 'dado' não for um float
            servidor.sendto("O valor digitado é inválido", cliente_endereco)
    #Finalizando servidor
    servidor.close()
            
        

if __name__ == '__main__':
    main()
