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
    s.send(b'levelx13')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    data2=data2.decode('utf-8')
    soln=[]
    temp=''
    for i in data2:
        if i not in [' ','[',']']:
            temp+=i
        else:
            soln.append(temp)
            temp=''
    
    print('Resulting list would be: ',soln)
    soln.sort()
    print(soln,'is the sorted solution.')
    # Send the challenge solved / Envia el resultado del challenge.
    data2=soln[-1]
    print('Sending the challenge')
    data2=data2.encode('utf-8')
    s.send(data2)
    
    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)
