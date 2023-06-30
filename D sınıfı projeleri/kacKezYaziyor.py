"""def kelime_ara(cumle, kelime):
    kelime_sayisi = cumle.lower().count(kelime.lower())
    return kelime_sayisi

cumle = input("Bir cümle girin: ")
aranacak_kelime = input("Aramak istediğiniz kelimeyi girin: ")

sonuc = kelime_ara(cumle, aranacak_kelime)
print("Belirttiğiniz kelime cümle içinde {} kez geçiyor.".format(sonuc))
"""

def kelime_ara(cumle, kelime):
    cumle = cumle.lower()
    kelime = kelime.lower()
    bulunan_konumlar = []
    index = 0

    while index < len(cumle):
        konum = cumle.find(kelime, index)
        if konum == -1:
            break
        bulunan_konumlar.append(konum)
        index = konum + len(kelime)

    return bulunan_konumlar


cumle = input("Bir cümle girin: ")
aranacak_kelime = input("Aramak istediğiniz kelimeyi girin: ")

sonuc = kelime_ara(cumle, aranacak_kelime)

if len(sonuc) == 0:
    print("Belirttiğiniz kelime cümle içinde bulunamadı.")
else:
    print("Belirttiğiniz kelime cümle içinde {} kez geçiyor.".format(len(sonuc)))
    print("Kelimenin konum(lar)ı: ", end="")
    for konum in sonuc:
        print(konum, end=" ")
