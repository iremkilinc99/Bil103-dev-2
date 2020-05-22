import socket

serverPort = 12000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('10.3.42.217',serverPort))
serverSocket.listen(1)

print("The server is ready to receive")


while 1:

    connectionSocket, addr = serverSocket.accept()
    byte_sentence = connectionSocket.recv(1024)
    utf_sentence = byte_sentence.decode("utf-8")

    if utf_sentence=="1 1":
       modified_utf_sentence="BİL 103 Bilgisayar Bilimlerine Giriş	2\nBİL 113 Bilgisayar Programlama I 4\nMAT 101	Matematik I	4\nFİZ 101 Fizik I 3\nFİZ 101L	Fizik I Laboratuvarı 1\nTÜR 101	Türk Dili I	2\nİNG 001	İngilizce I	2\nToplam Kredi	18"
    elif utf_sentence=="1 2" :
       modified_utf_sentence="BİL 211	Bilgisayar Programlama II 4 \nBİL 132	Bilgisayar Bilimleri İçin Ayrık Matematik	3\nMAT 102	Matematik II	4\nFİZ 102	Fizik II	3\nFİZ 102L	Fizik Laboratuvarı II	1\nTÜR 102	Türk Dili II	2\nİNG 002	İngilizce II	2\nToplam Kredi	19"
    elif utf_sentence=="2 1" :
       modified_utf_sentence="BİL 133	Kombinatorik ve Çizge Kuramı	3\nBİL 212	Veri Yapıları	4\nBİL 264	Mantıksal Devre Tasarımı	3\nBİL 264L	Mantıksal Devre Tasarımı Laboratuvarı	1\nMAT 203	Lineer Cebir ve Dif. Denklemlere Giriş	4\nAİT 201	Atatürk İlkeleri ve İnkılâp Tarihi I	2\nİNG 003	İngilizce Yazma Becerileri	2\nToplam Kredi	19"
    elif utf_sentence=="2 2":
       modified_utf_sentence="BİL 331	Algoritma Analizi	3\nBİL 395	Programlama Dilleri	3\nBİL 481	Yazılım Mühendisliği	3\nEND 213	Olasılık ve İstatistik I	3\nUGİ 315	Girişimcilik ve Liderlik	2\nİYD 1	İkinci Yabancı Dil I	3 \nToplam Kredi	17"
    elif utf_sentence=="2 3" : 
       modified_utf_sentence="OEG 200	Ortak Eğitim I	0\nToplam Kredi	0"
    elif utf_sentence=="3 1" :
       modified_utf_sentence="BİL 372	Veritabanı Sistemleri	4\nBİL 461	İşletim Sistemleri	3\nSeçmeli Ders	3\nBölüm Seçmeli Dersi I	3\nİYD 2	İkinci Yabancı Dil II	3\nToplam Kredi	16"
    elif utf_sentence=="3 2" :
       modified_utf_sentence="OEG 300	Ortak Eğitim II	0\nToplam Kredi	0"
    elif utf_sentence=="3 3" :
       modified_utf_sentence="BİL 452	Veri İletişimi ve Bilgisayar Ağları	3\nBİL 495	Yenilikçi Bilgisayar Uygulamaları	1\nFakülte Seçmeli Dersi	3\nBölüm Seçmeli Dersi II	3\nBölüm Seçmeli Dersi III	3\nİYD 3	İkinci Yabancı Dil III	3\nToplam Kredi	16"
    elif utf_sentence=="4 1" :
       modified_utf_sentence="OEG 400	Ortak Eğitim II	0\nToplam Kredi	0"
    elif utf_sentence=="4 2" :
       modified_utf_sentence="BİL 496	Bitirme Projesi	4\nBölüm Seçmeli Dersi IV	3\nBölüm Seçmeli Dersi V	3\nÜniversite Seçmeli Dersi	3\nİYD 4	İkinci Yabancı Dil IV	3\nToplam Kredi	16"
    else :
        modified_utf_sentence="invalid"
        print("Hazirlayan: \nİrem Kılınç 171101036\n")
        break

    modified_byte_sentence = bytes(modified_utf_sentence, "utf-8")
    connectionSocket.send(modified_byte_sentence)
    connectionSocket.close()
