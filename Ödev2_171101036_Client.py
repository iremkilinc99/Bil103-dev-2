import socket

ip = input("Enter your IP address: ")
port = 12000

while 1:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((ip, port))

    utf_sentence = input("istediğiniz yıl ve dönemi arada boşluk olacak şekilde giriniz 1 1 ya da 3 3 gibi")
    byte_message = bytes(utf_sentence, "utf-8")
    clientSocket.send(byte_message)

    modified_byte_sentence = clientSocket.recv(1024)
    modified_utf_sentence = modified_byte_sentence.decode("utf-8")

    if modified_utf_sentence=="invalid":
     print("Hazirlayan: \nİrem Kılınç 171101036\n")
     break;

    print(modified_utf_sentence)
    clientSocket.close()
