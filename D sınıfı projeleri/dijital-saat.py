import tkinter as tk
import time

def update_time():
    saat = time.strftime("%H:%M:%S")
    label.config(text=saat)
    label.after(1000, update_time)

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Dijital Saat")

# Etiket oluştur
label = tk.Label(pencere, font=("Arial", 80), bg="black", fg="white")
label.pack(pady=50)

# Saati güncelle
update_time()

# Pencereyi göster
pencere.mainloop()


"""tkinter.Tk(): Tk() sınıfı, tkinter modülünün bir parçasıdır ve bir pencere oluşturmak için kullanılır. pencere = tk.Tk() satırıyla bir pencere nesnesi oluşturulur.

pencere.title("Dijital Saat"): title() metodu, pencere nesnesi üzerinde çağrıldığında pencere başlığını ayarlar. Burada "Dijital Saat" başlığı kullanılır.

tkinter.Label(): Label() sınıfı, bir etiket oluşturmak için kullanılır. label = tk.Label(pencere, font=("Arial", 80), bg="black", fg="white") satırıyla bir label nesnesi oluşturulur. Parametreler aracılığıyla etiketin özellikleri belirlenir. pencere nesnesi, etiketin hangi pencereye ait olacağını belirtir. font parametresi, metnin fontunu belirler. bg parametresi, etiketin arka plan rengini belirler. fg parametresi, metin rengini belirler.

label.config(text=saat): config() metodu, etiketin özelliklerini güncellemek için kullanılır. Bu örnekte text özelliği, etiketin metnini temsil eder. saat değişkeni, metnin içeriğini tutar. Bu satır, etiketin metnini günceller ve saat değişkenindeki saat bilgisini gösterir.

label.pack(pady=50): pack() metodu, etiketi pencere içindeki yerini belirlemek için kullanılır. pady parametresi, etiketin üst ve alt kenarları arasındaki yatay boşluğu ayarlar.

label.after(1000, update_time): after() metodu, belirli bir süre sonra belirli bir işlevi çağırmak için kullanılır. Bu örnekte 1 saniye (1000 ms) bekledikten sonra update_time() işlevini çağırır. Bu, saat bilgisinin her saniye güncellenmesini sağlar.

pencere.mainloop(): mainloop() metodu, pencereye ait olayları yakalamak ve uygulamayı çalıştırmak için kullanılır. Bu kod, pencerenin görüntülenmesini ve kullanıcı etkileşimlerini bekler. Program burada durmaya devam eder, kullanıcı pencereyi kapattığında çalışmayı sonlandırır.
    """