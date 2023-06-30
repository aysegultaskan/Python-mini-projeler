import random

def sihirli_sekiz_top():
    cevaplar = [
        "Kesinlikle öyle.",
        "Kuşkusuz.",
        "Kesinlikle.",
        "Evet, kesinlikle.",
        "Buna güvenebilirsin.",
        "Görünüşe göre evet.",
        "Büyük olasılıkla.",
        "Evet.",
        "Belki.",
        "Cevabım bulanık, tekrar dene.",
        "Daha sonra sor.",
        "Şimdi söylemesem daha iyi.",
        "Tahmin edemem.",
        "Konsantre ol ve tekrar sor.",
        "Cevabım hayır.",
        "Kaynaklarım hayır diyor.",
        "Görünüşe göre hayır.",
        "Kesinlikle hayır.",
        "Yanıtımı tekrar düşünmen gerekebilir."
    ]
    
    print("Sihirli Sekiz Topa hoş geldiniz!")
    print("Bir soru sorun ve cevabı öğrenin.")
    
    while True:
        soru = input("Soru: ")
        if soru.lower() == "çıkış":
            print("Sihirli Sekiz Top'a veda ediyor.")
            break
        
        cevap = random.choice(cevaplar)
        print("Cevap:", cevap)
        print()

sihirli_sekiz_top()
