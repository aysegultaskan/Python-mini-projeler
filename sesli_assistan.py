import speech_recognition as sr  #çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from datetime import datetime  #anlık zamanı öğrenmek için
import webbrowser  #web browser açmak için
import time  #bilgisayrı uyutmak için
from gtts import gTTS   #text i ses e çevirmek için
from playsound import playsound  #ses dosyasını çalmak için
import random  #random bir sayı üretmek için
from random import choice  #random bir değer seçmek için
import os  #sistem ayarları değiştirmk için
from lxml import html  #html dosyasını okumak için
import requests  #istek göndermek için
import json   #json dosyalarını okumak için
import feedparser  #hava  durumunu çekmek için
import colorama  #terminal ekranını özelleştirmek için
from colorama import Fore, Back, Style   #Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.

r=sr.Recognizer() #speech recognition ile alınan sesi r adlı değikene atıyoruz

colorama.init()

def record(ask = False): #record adlı bir fonksiyon oluşturuyoruz ve varsayılan olarak ask =false olarak ayarlıyouz
    
    try:

        with sr.Microphone() as source: #mikrofandan gelen veriyi işlem yapabilmek için source e tanımlıyoruz
            if ask:
                speak(ask)
                print(Fore.BLUE)
                print(ask)

            audio = r.listen(source) #dinlenilen source u audio ya atıyoruz
            voice = ''
            try: 
                voice = r.recognize_google(audio,language='tr-TR')  #Türkçe dinleme yapıp bunu voice e atıyoruz
                return voice #dinlediğimiz voice ı geri döndürüyoruz
            except sr.UnknownValueError: #gelen sesi tanımlayamazsa burası çalışıyor
                
                print(Fore.RED)
                print("ne dedin, anlamadım, acaba tekrar edermisin")
                speak("ne dedin, anlamadım, acaba tekrar edermisin")
                
    except sr.RequestError: #eğerki sistemle alakalı bir hata alırsak burası çalışıyor
        speak('Sistemin çalışmıyor')
        print(Fore.GREEN)
        print('Sistemin çalışmıyor')
        
def response(voice):  #voice ile gelen veriyi sorgululamak için response adında bir fonkiyon
    if 'nasılsın' in voice:  #eğer voice nin içinde nasılsın  diye bir değer varsa bunları yap
        sozler = ["iyiyim ya sen",
                "iyi ben peki ya sen",
                "teşekkür ederim iyiyim. Sen nasılsın",
                
        ]
        secim=choice(sozler)  #sozlerden birini karışık olarak seçilecek

        speak(secim)  #seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Betty  = "+secim)  #seçilen söz yazdırılacak
          
        
    if 'iyiyim' in voice:  #eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Betty  = iyi olmana sevindim senin için ne yapabilirim")  #ekrana yazılacak veri
        speak("iyi olmana sevindim senin için ne yapabilirim")  #sesli bir şekilde söylenmesi için           
    
    if 'teşekkür ederim'  in voice:  #eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Betty  = ne demek her zaman")  #ekrana yazılacak veri
        speak("ne demek her zaman")  #sesli bir şekilde söylenmesi için    
    
    if 'saat kaç' in voice: #eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
        speak(datetime.now().strftime('%H:%M:%S')) #datetime.now sayesinde anlık saati alıyor ve seslendiriyor
        print(Fore.GREEN)
        print("Betty  = "+datetime.now().strftime('%H:%M:%S')) #datetime.now sayesinde anlık saati alıyoruz ve yazdırıyoruz

    if 'arama yap' in voice: #eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        search = record('ne aramamı istersin')  #record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp search değişkenine tanımlıyoruz
        url ='https://google.com/search?q='+search  #https://google.com/search?q= adresine aldığımız search ı ekliyoruz ve url değişkenine tanımlıyoruz
        webbrowser.get().open(url)  #web browserı açıyouz ve  url değişkenini dönderiyoruz
        speak(search+' için bulduğum sonuçlar')  #sesli bir şekilde seslendirme yapıyoruz
        print(Fore.GREEN)
        print("Betty  = "+search+' için bulduğum sonuçlar')  #ekrana yazdırma yapıyoruz
    
    if 'güle güle' in voice:  #eğer voice nin içinde güle güle diye bir değer varsa bunları yap
        speak('görüşürüz') #sesli söyletiyoruz
        print(Fore.GREEN)
        print('Betty  = görüşürüz') #ekrana yazdırıyoruz
        exit() #uygulamadan çıkış yapıyoruz   
    
def speak(string):  #speak adlı bir fonksiyon oluştuyoruz 
    tts = gTTS(string,lang='tr')  #sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyoruz
    file= 'ses-'+str(time.time_ns())+'.mp3'  #.mp3 uzantılı bir ses dosyası oluşturuyoruz
    tts.save(file)   #dosyayı kayıt ediyoruz
    playsound(file)  #dosyayı okutuyoyz
    os.remove(file)  #dosyayı siliyouz
    
print(Fore.GREEN)
print('Merhaba ben Betty seni dinliyorum senin için ne yapabilirim')  #ilk açılışta asiatanın bizi karşılamasını yazdırmak için

speak('Merhaba ben Betty seni dinliyorum senin için ne yapabilirim')  #ilk açılışta asiatanın bizi karşılaması için
time.sleep(.5)  #uygulamyı  uyutuyoruz dinlemede karışıklık olmaması için

while True:  #tek bir komut aldıktan sonra kapanmaması için sonsuz döngü oluşturuyoruz
    voice=record()
    print(Fore.BLUE)
    print(voice)
    response(voice)
    print(Fore.GREEN)
    #speak('Başka bir isteğin varmı')
    #print('BAŞKA BİR İSTEĞİN VARMI')      
        
        