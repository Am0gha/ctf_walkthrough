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
    s.send(b'levelx12')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    soln=data2.decode('utf-8')
    sub=''

    for i in range(len(soln)):
        if soln[i]!=' ':
            sub+=soln[i]
        else:
            num=soln[i+1]+soln[i+2]
            num=int(num)
            print(num)
            break

    fin=sub*num
    print(fin)
    fin=fin.encode('utf-8')
    print(fin)
    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending the challenge')
    s.send(fin)

    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)

