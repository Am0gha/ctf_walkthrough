'''
You will receive a string, you must return the same string and you will
receive another string which you must also return.
'''

import socket
#import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx01" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx01')
    # Change the text to the level you want to attempt.

    # You will be receiving the input required using the recv()
    # function with 1024 as as the arguement, if mentioned
    # that you are receiving multiple inputs then invoke the same
    # method with the same arguement to receive the new input,
    # but make sure you are saving the new input in a different
    # variable

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    # Sending the first challenge
    print('Sending the first challenge')
    s.send(data2)
    
    # You would be sending the output using the send() function.
    # Make sure that before sending the output you would convert
    # it into bytes or encode it into utf-8 format.

    # Receiving the second challenge
    print('Receiving challenge 2.')
    data3 = s.recv(1024)

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending second challenge')
    s.send(data3)

    # Receive the flag / Recibe la flag.
    print('Receiving flag')
    data3 = s.recv(1024)
    print(data3)

