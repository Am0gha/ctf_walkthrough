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
    s.send(b'levelx10')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)

    inpt=data2.decode('utf-8')
    lst=list(inpt)

    for i in range(len(lst)):
        if lst[i]==' ':
            lst[i]=','
    
    num=''
    num_lst=[]

    print('Converting the list of numbers in string to integers.')
    for i in range(len(lst)):
        if i==len(lst)-1:
            num+=lst[i]
            num_lst.append(int(num))
            num=''
        elif lst[i]!=',':
            num+=lst[i]
        elif lst[i]==',' or i==len(lst)-1:
            num_lst.append(int(num))
            num=''
    
    num_lst.sort()
    ans=''
    
    print('Concatenating the sorted list as a string of numbers')
    for i in num_lst:
        ans+=(str(i))

    ans=ans.encode('utf-8')
    print(ans)
    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending the challenge')
    s.send(ans)

    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)

