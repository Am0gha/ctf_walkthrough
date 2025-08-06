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
    s.send(b'levelx09')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)
    tst=data2.decode('utf-8')
    l='abcdefghijklmnopqrstuvwxyz'
    u=l.upper()
    ans=''
    for i in tst:
        print(i,end=' ')
        if 'a'<=i<='z':
            ans+=l[l.index(i)-13]
        elif 'A'<=i<='Z':
            ans+=u[u.index(i)-13]
        else:
            ans+=i
    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending the challenge')
    s.send(ans.encode('utf-8'))

    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)

