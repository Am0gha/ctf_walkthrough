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

    dic={'.----':'1',
         '..---':'2',
         '...--':'3',
         '....-':'4',
         '.....':'5',
         '-....':'6',
         '--...':'7',
         '---..':'8',
         '----.':'9',
         '-----':'0',
         '.-':'A',
         '-...':'B',
         '-.-.':'C',
         '-..':'D',
         '.':'E',
         '..-.':'F',
         '--.':'G',
         '....':'H',
         '..':'I',
         '.---':'J',
         '-.-':'K',
         '.-..':'L',
         '--':'M',
         '-.':'N',
         '---':'O',
         '.--.':'P',
         '--.-':'Q',
         '.-.':'R',
         '...':'S',
         '-':'T',
         '..-':'U',
         '...-':'V',
         '.--':'W',
         '-..-':'X',
         '-.--':'Y',
         '--..':'Z'
    }

    # Send "levelx00" to choose the level / Envia levelx00 para elegir el nivel.
    s.send(b'levelx11')

    # Receive the challenge / Recibe el challenge.
    print('Receiving challenge.')
    data2 = s.recv(1024)
    print(data2)
    morse=data2.decode('utf-8')
    sub_str=''
    ans=''

    for i in range(len(morse)):
        if i==len(morse)-1:
            sub_str+=morse[i]
            ans+=dic[sub_str]
            sub_str=''
        elif morse[i]!=' ':
            sub_str+=morse[i]
        else:
            ans+=dic[sub_str]
            sub_str=''
    soln=ans.encode('utf-8')

    # Send the challenge solved / Envia el resultado del challenge.
    print('Sending the challenge')
    s.send(soln)

    # Receive the flag / Recibe la flag.
    print('Receiving the flag')
    data3 = s.recv(1024)
    print(data3)

