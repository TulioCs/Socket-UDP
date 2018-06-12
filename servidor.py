# -*- coding: utf-8 -*-
import socket
from datetime import datetime
import statistics
servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#comunicação ipv4 e socket udp
IP = '192.168.43.171'
porta = 5002
buffer_size = 1024
servidor.bind((IP,porta))


def get_dados ():
    dados = open('dados.txt','r')
    temperatura = []
    for line in dados:
        x , y = line.split(';')
        temperatura.append(float(x))
    dados.close()
    return temperatura

def media (list_tmp):
    return statistics.mean(list_tmp)

def mediana (list_tmp):
    return statistics.median(list_tmp)

def moda (list_tmp):
    return statistics.mode(list_tmp)

def main():
    while True:
       
        data,endereco = servidor.recvfrom(buffer_size)
        
        if (data == 'A'):
            list_tmp = get_dados()
            servidor.sendto(str(media(list_tmp)), endereco)
        
        elif(data == 'B'):
            list_tmp = get_dados()
            servidor.sendto(str(mediana(list_tmp)), endereco)
        
        elif (data == 'C'):
            list_tmp = get_dados()
            servidor.sendto(str(moda(list_tmp)), endereco)
        
        else:
            dados = open('dados.txt','a+')
            now = datetime.now()
            dados.write(data)
            dados.write(";")
            dados.write(str(now) + "\n")
            dados.close()
            
        

if __name__ == '__main__':
    main()
