"""
PROJE1
isim1 = input("Senin ismin: ")
isim2 = input("Diğer isim: ")

love = len(isim1) + len(isim2)
if len(isim1) > len(isim2):
    love -=5
else:
    love +=3
    
love *=42
love = love/ (100 + len(isim2))

love = 10 if love > 10 else round(love,0)

print("{} ve {} aşk dereceniz {}".format(isim1, isim2, love))
"""

#PROJE2
import random

def ask_yuzdesi(isim1, isim2):
    isim1 = isim1.lower()
    isim2 = isim2.lower()
    
    toplam_harfler = isim1 + isim2
    harf_listesi = list(set(toplam_harfler))
    
    ask_skoru = 0
    for harf in harf_listesi:
        ask_skoru += toplam_harfler.count(harf)
    
    sevgi_skoru = ask_skoru % 101
    return sevgi_skoru

isim1 = input("Birinci kişinin adını girin: ")
isim2 = input("İkinci kişinin adını girin: ")

sonuc = ask_yuzdesi(isim1, isim2)
print("{} ve {} için aşk yüzdesi: {}%".format(isim1, isim2, sonuc))

