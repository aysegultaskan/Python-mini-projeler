def kelime_sayisi(metin, kelime):
    kelime_listesi = metin.split()  # Metni boşluklardan ayırarak kelime listesine dönüştürdük
    sayac = 0
    for kelime_metin in kelime_listesi:
        if kelime_metin == kelime:  # Girilen kelimeyle metindeki her bir kelimeyi karşılaştırırdık
            sayac += 1  # Eşleşme bulunduğunda sayaç değişkenini artırırız
    return sayac

# Kullanıcıdan metin dosyasının adını ve aranacak kelimeyi aldık
dosya_adi = input("Metin dosyasının adını girin: ")
kelime = input("Hangi kelimeyi aramak istiyorsunuz? ")

#try-except bloğu kullanarak dosyanın açılmasını ve metnin okunmasını gerçekleştirdik
try:
    # Dosyayı açar ve metni okur (utf-8 karakter kodlamasıyla)
    with open(dosya_adi, 'r', encoding='utf-8') as dosya: #'r', open() fonksiyonunda kullanılan bir dosya modudur ve "read" anlamına gelir
        metin = dosya.read()
        sayac = kelime_sayisi(metin, kelime)  # Girilen kelimenin metin içinde kaç kez geçtiğini bulduk
        print("Girilen kelime metin içinde", sayac, "kez geçiyor.")

#Dosya bulunamazsa        
except FileNotFoundError:
    print("Dosya bulunamadı!?")
    

