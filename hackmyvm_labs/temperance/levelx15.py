import socket
import base64

HOST = "temperance.hackmyvm.eu"
PORT = 9988

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Connect to the host and receive the message / Conecta al host y recibes la intro general.
    print('Receiving Intro')
    data = s.recv(1024)
    print(data)

    # Send "levelx00" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx15')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)
    
    data2=data2.decode('utf-8')
    print(type(data2))
    print(data2)
    last='['
    for i in data2:
        if i!=' ':
            last+=i
        else:
            last+=','
    last+=']'
    lst=eval(last)
    diff=lst[1]-lst[0]
    res=lst[-1]+diff
    data2=str(res).encode('utf-8')
    
    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending the challenge')
    s.send(data2)

    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)

