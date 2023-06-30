from datetime import datetime
import random

def replik_yaz():
    replikler = ["Sen ölmeyi bayılmak mı zannediyorsun",
                 "Birde bayıl istersen Feriha",
                 "Kızımın peşini bırakmak için ne kadar istyorsun",
                 "Sen Bihter Ziyagil'sin aptallık etme",
                 "Ölüm ölüm dediği nedir ki gülüm. Ben senin için yaşamayı göze almışım.",
                 "Aman Ali Rıza Bey ağzımızın tadı kaçmasın.",
                 "Onunla ben evlenicem!",
                 "Size baba diyebilir miyim amca?",
                 "Ömrümü yedin lan Jale!",
                 "Sakın tek bir kelime daha edeyim deme! Neden biliyor musun? Çünkü inanırım.",
                 "Sevim koş, katil geldi",
                 "Biz ayrı dünyaların insanlarıyız",
                 "N'ayır N'olamaz!",
                 "O gemi bir gün gelecek",
                 "Beni beni Bihter'ini",
                 "Peki, Zeki Müren de bizi görecek mi? Hayır yani görecekse bilelim. Sadece Zeki Müren olsa iyi. Bunun reis-i cumhuru var, başbakanı var",
                 "Tutmayın küçük enişteyi, salıverin gitsin",
                 "Senin annen bir melekti yavrum",
                 "Güzel olduğunuz kadar küstahsınız da",
                 "Evlenince pembe pancurlu bir evimiz olacak",
                 "Yaptım, yaptım ama bir sor niye yaptım"
    ]
    
    
    
    while True:   
         
        replik = random.choice(replikler)
        print("Bu repliği yazmaya çalış:", replik)

        saniyeBasla = datetime.now()
        kullanici_replik = input("Repliği yazın: ")
        saniyeBitir = datetime.now()
        saniyeFarki = saniyeBitir - saniyeBasla
        seconds = saniyeFarki.total_seconds() #bu adımda süreyi saniyelere dönüştürmek için total_seconds() metodunu kullanık. seconds değişkeni, kullanıcının repliği yazma süresini saniye cinsinden ifade eder.
    
        if kullanici_replik == replik:
            print("Tebrikler! Repliği doğru yazdınız.")
        else:
            print("Maalesef yanlış yazdınız.")

        print("Geçen süre: {:.2f} saniye.".format(seconds)) # seconds değişkeni, geçen süreyi saniye cinsinden tuttuğu için bu satırda ekrana yazdırılır. "{:.2f}" formatı, süreyi virgülden sonra iki basamaklı olarak göstermek için kullanılır.


replik_yaz()

    
    
    