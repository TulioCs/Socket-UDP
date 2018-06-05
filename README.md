# Socket-UDP

This project aims to create a simple UDP (User Datagram Protocol) Socket. This socket has two clients (the sender and the receiver) and one server. The sender client it will simulate a temperature sensor reading, i.e. it'll get a random number and send it to the server to be saved in a file. The receiver client will send an option (A, B or C) to the server to select with operation he wants to get, the operations are: A. Média (Mean), B. Mediana (Median) and C. Moda (Mode). Depending the operation selected, the server will do this operation and send the result back to the client. All temperatures are saved in a text file (dados.txt) with the date and time when this measurement was got.

## Getting Started

These instructions will show how to use this project on your local machine for deployment and testing purposes.

### Python Versions used
```
Python 2.7.12 and Python 2.7.14
```

### Prerequisites

The prerequisites of this project are the libraries:

* [Statistics](http://cpython-test-docs.readthedocs.io/en/latest/library/statistics.html) - To calculate the Mean, Median and Mode;

```
$ sudo pip install statistics
```

* [Socket](https://docs.python.org/2.7/howto/sockets.html) - To work with the UDP Socket;
* [Datetime](https://docs.python.org/2/library/datetime.html) - To get the actual time and date;
* [Random](https://docs.python.org/2/library/random.html?highlight=random#module-random) - To get random numbers.

Socket, datetime and random modules are already included in the python standard library.

### Running

#### Locally

To test the project, you must to configure your server by setting the IP, the port and the message buffer size at the server code (servidor.py), for example:

```
IP = '127.0.0.1'

porta = 5002

buffer_size = 1024
```

And after that, you need to set the same ID and port at the cliente_send_py and cliente_receiver.py files.

#### Remotely at the same network
To run the project remotely, you'll change the same lines that you changed to run locally. The only difference is that the IP will change. If you are using two computers, for example, one of them will be the server and the other will be the client.

At the server computer you'll get it's IP, set it at the servidor.py IP line and run the server code:
```
$ python servidor.py
```

At the client computer, you'll get the same server IP and set at the client IP line, and then run it.
```
$ python cliente_send.py
```

or

```
$ python cliente_receiver.py
```

And that's it.

<!-- ## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). -->

## Authors

* **Tulio Campos** - *Initial work* - [Socket-UDP](https://github.com/TulioCs/Socket-UDP)
* **Levy Santiago** - *This repository* - [Socket-UDP](https://github.com/Levysantiago/Socket-UDP)

<!-- See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project. -->

## Acknowledgments

* [Socket Documentation](https://docs.python.org/2/library/socket.html) - Where the code was based.
