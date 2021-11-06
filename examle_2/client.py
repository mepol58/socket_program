import socket                

# Socket oluşturulması
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


# Bağlanılacak adres ve port
host = "localhost"
serverPort = 12345                

try:
    # Bağlantıyı yap
    clientSocket.connect((host, serverPort))
    utf_sentence = input("lowecase input please: ")
    byte_sentence=bytes(utf_sentence,"utf-8")
    clientSocket.send(byte_sentence)

    # serverden yanıtı al
    modified_bytesentence = clientSocket.recv(1024)
    modified_utfsentence= modified_bytesentence.decode("utf-8")
    print("capitalized sentence: ",modified_utfsentence)

    # bağlantıyı kapat
    clientSocket.close() 
except socket.error as msg:
    print("[Server aktif değil.] Mesaj:", msg)
