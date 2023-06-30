import random

def sekiz_topu():
    secimler = ["Evet Kesinlikle",
             "Kuşkusuz", 
             "%100",
             "Eminim ki isteyin olacak",
             "Büyük olasılıkla",
             "Kesinlikle",
             "Üzgünüm",
             "Cevap vermesem daha iyi olacak",
             "Emin değilim",
             "Olamayabilir",
             "Sanmıyorum",
             "Hayır",
             "Asla"
    ]
    
    print("Sihirli Sekiz Top Oyununa Hoş Geldiniz :)")
    
    while True:
        soru = input("Sorunuzu sorun: ")
        if soru== "çıkış":
            print("Oyundan Çıkış Yaptınız!")
            break
        
        secim = random.choice(secimler)
        print("Cevabım: ", secim)
       
        
sekiz_topu()