import random

# Oyun tahtası oluşturma
def tahta_olustur():
    tahta = [[0] * 4 for _ in range(4)]
    return tahta

# Yeni sayı ekleme
def yeni_sayi(tahta):
    empty_cells = []

    for y in range(4):
        for x in range(4):
            if tahta[y][x] == 0:
                empty_cells.append((y, x))

    if len(empty_cells) == 0:
        print("Oyun bitti. Boş hücre kalmadı.")
        return

    y, x = random.choice(empty_cells)
    tahta[y][x] = random.choice([2, 4])

# Tahtayı ekrana yazdırma
def tahta_yazdir(tahta):
    for row in tahta:
        for element in row:
            print(element, end="\t")
        print()

# Yukarı hareket
def yukari_hareket(tahta):
    for x in range(4):
        kolon = [tahta[y][x] for y in range(4)]
        kolon = birlestir(kolon)
        for y in range(4):
            tahta[y][x] = kolon[y]

# Sol hareket
def sol_hareket(tahta):
    for y in range(4):
        satir = tahta[y]
        satir = birlestir(satir)
        tahta[y] = satir

# Aşağı hareket
def asagi_hareket(tahta):
    for x in range(4):
        kolon = [tahta[y][x] for y in range(4)][::-1]
        kolon = birlestir(kolon)[::-1]
        for y in range(4):
            tahta[y][x] = kolon[y]

# Sağ hareket
def sag_hareket(tahta):
    for y in range(4):
        satir = tahta[y][::-1]
        satir = birlestir(satir)[::-1]
        tahta[y] = satir

# Sıralama ve birleştirme
def birlestir(lst):
    siralanmis = [element for element in lst if element != 0]
    for i in range(len(siralanmis) - 1):
        if siralanmis[i] == siralanmis[i+1]:
            siralanmis[i] *= 2
            siralanmis[i+1] = 0
    siralanmis = [element for element in siralanmis if element != 0]
    siralanmis += [0] * (len(lst) - len(siralanmis))
    return siralanmis

# Oyun döngüsü
def oyun():
    tahta = tahta_olustur()

    yeni_sayi(tahta)
    yeni_sayi(tahta)
    tahta_yazdir(tahta)

    while True:
        hareket = input("Yön seçin (w/a/s/d): ")

        if hareket == "w":
            yukari_hareket(tahta)
        elif hareket == "a":
            sol_hareket(tahta)
        elif hareket == "s":
            asagi_hareket(tahta)
        elif hareket == "d":
                        sag_hareket(tahta)
        else:
            print("Geçersiz hareket. Tekrar deneyin.")

        tahta_yazdir(tahta)
        yeni_sayi(tahta)

# Oyunu başlat
oyun()

