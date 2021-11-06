import socket

host = "localhost"
port = 12345


try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("socket oluşturuldu")

    serverSocket.bind((host, port)) 
    print("socket {} nolu porta bağlandı".format(port))

    s.listen(5)      
    print("socket is ready")
except socket.error as msg:
    print("error:",msg)

while True: 

   # Client ile bağlantı kurulursa 
   connectionSocket, addr = serverSocket.accept()
   byte_sentence=connectionSocket.recv(1024)
   utf_sentence=byte_sentence.decode("utf-8")
   modified_utfsentence=utf_sentence.upper()
   
   connectionSocket.send(modified_utfsentence)
   connectionSocket.close()

   # Bağlantıyı sonlandıralım 

