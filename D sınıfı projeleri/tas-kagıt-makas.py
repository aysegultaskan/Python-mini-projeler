import random

print(("-" * 30) + "\nTaş, Kağıt, Makas\n" + ("-" * 30))

kullanici_skoru, bilgisayar_skoru = 0, 0

while True:
    print("\n1 - Taş\n2 - Kağıt\n3 - Makas")
    secim = input("Hangisini seçeceksin: ")
    bil_secim = random.choice(["1", "2", "3"])

    if secim not in ["1", "2", "3"]:
        print("Yanlış bir seçim yaptınız!")
        break

    secimler = {"1": "Taş", "2": "Kağıt", "3": "Makas"}

    print("Bilgisayarın seçimi:", secimler[bil_secim])

    if secim == bil_secim:
        print("Sonuç berabere")
    elif (secim == "1" and bil_secim == "3") or (secim == "2" and bil_secim == "1") or (secim == "3" and bil_secim == "2"):
        print("Kazandınız!")
        kullanici_skoru += 1
    else:
        print("Kaybettiniz")
        bilgisayar_skoru += 1

    print("\nKullanıcı Skoru: {}\nBilgisayarın Skoru: {}".format(kullanici_skoru, bilgisayar_skoru))
    
    