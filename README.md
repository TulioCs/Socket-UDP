# Project Title

This project aims to create a simple UDP (User Datagram Protocol) Socket. This socket has two clients (the sender and the receiver) and one server. The sender client it will simulate a temperature sensor reading, i.e. it'll get a random number and send it to the server to be saved in a file. The receiver client will send an option (A, B or C) to the server to select with operation he wants to get, the operations are: A. Média (Average), B. Mediana (Median) and C. Moda (Mode). Depending the operation selected, the server will do this operation and send the result back to the client. All temperatures are saved in a text file (dados.txt) with the date and time when this measurement was got.

