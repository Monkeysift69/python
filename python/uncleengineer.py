wordlist = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']
text = []
import random
import socket

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server.connect(('104.248.39.146', 27617))

while len(text) != 8000:
    w1 = random.choice(wordlist)
    w2 = random.choice(wordlist)
    w3 = random.choice(wordlist)
    t = w1 + '-' + w2 + '-' + w3
    if t not in text:
        text.append(t)
        server.send(t.encode('utf-8'))

        data_server = server.recv(1024).decode('utf-8')
        print(data_server)
        print(t)

server.close()